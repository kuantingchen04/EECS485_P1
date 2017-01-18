from flask import *
from extensions import connect_to_database
import os
from werkzeug.utils import secure_filename
import hashlib
import datetime, time


### defines ###

album = Blueprint('album', __name__, template_folder='templates')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'bmp', 'gif'])
IMG_DIR = 'static/images'


### functions ###

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_picid_lst(albumid):
    image_names = [ filename
                    for filename in os.listdir(IMG_DIR)
                    if filename.endswith(tuple(ALLOWED_EXTENSIONS))]
    db = connect_to_database()
    cur = db.cursor()

    picid_lst = []
    q = 'SELECT sequencenum ,picid FROM Contain WHERE albumid="%s"' % albumid
    cur.execute(q)
    results = cur.fetchall()
    for result in results:
        pic_id_type = [ x 
                    for x in image_names 
                    if x.split('.')[0] == result['picid'] ]
        
        # debug
        if not pic_id_type[0]:
            print('ERROR! Cant find image file')
        picid_lst.append(pic_id_type[0])

        #print([result['sequencenum'],pic_id_type[0]])
    #print('albumid: %s' % albumid)
    #print('# of images: %s' % len(results))
    return picid_lst

def add_image_db(albumid,filename):
    db = connect_to_database()
    cur = db.cursor()

    # current info
    cur.execute('SELECT sequencenum, albumid, picid, caption FROM Contain')
    results = cur.fetchall()
    current_seqnum = results[-1]['sequencenum']

    print('num of photos: %s, latest sequencenum: %s' % (len(results),current_seqnum))

    
    # update Photo Instance
    m = hashlib.md5((str(albumid) + filename).encode('utf-8'))
    picid = m.hexdigest()
    picformat = filename.rsplit('.', 1)[1].lower()
   
    picdate = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    #picdate="TIMESTAMP '%s'" % st


    q = 'INSERT INTO Photo (picid, format, date) VALUES ("%s","%s",TIMESTAMP "%s")' % (picid,picformat,picdate)
    print('query:%s' % q)
    cur.execute(q)
    
    # update Contain Instance
    q = 'INSERT INTO Contain (sequencenum, albumid, picid, caption) VALUES (%s,%s,"%s","")' % (current_seqnum+1,int(albumid),picid)
    print('query:%s' % q)
    cur.execute(q)
    
    # update the Album info
    albumdate = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    q = 'UPDATE Album A SET A.lastupdated=TIMESTAMP "%s" WHERE A.albumid=%s' % (albumdate,albumid)
    print('query:%s' % q)
    cur.execute(q)

    return ''

def delete_image_db(albumid,picid):
    db = connect_to_database()
    cur = db.cursor()

    # current info
    cur.execute('SELECT sequencenum, albumid, picid, caption FROM Contain')
    results = cur.fetchall()
    current_seqnum = results[-1]['sequencenum']

    print('num of photos: %s, latest sequencenum: %s' % (len(results),current_seqnum))   


    # delete image from dircectory

    #os.remove() 
    # POT
    q = 'SELECT format FROM Photo WHERE picid = "%s"' % (picid)
    print('query:%s' % q)
    cur.execute(q)
    results = cur.fetchall()
    #print(results[0]['format'])
    ext = results[0]['format']

    target = os.path.join(APP_ROOT,'../static/images')
    destination = "/".join([target,'%s.%s' % (picid,ext)])

    print('QQ: %s'  % destination)
    os.remove(destination) 


    # delete from Contain Instance
    q = 'DELETE FROM Contain WHERE picid = "%s"' % (picid)
    print('query:%s' % q)
    cur.execute(q)

    # delete from Photo Instance
    q = 'DELETE FROM Photo WHERE picid = "%s"' % (picid)
    print('query:%s' % q)
    cur.execute(q)
    
    # update the Album info
    albumdate = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    q = 'UPDATE Album A SET A.lastupdated=TIMESTAMP "%s" WHERE A.albumid=%s' % (albumdate,albumid) 
    print('query:%s' % q)
    cur.execute(q)



    return



### routes ###

@album.route('/album/edit',methods=['GET','POST'])
def album_edit_route():
    options = {
        "edit": True
    }
    albumid_get = request.args.get('albumid', '')
    print('albumid_edit_route:%s' % albumid_get)


    
    if not albumid_get:
        print(404)
        abort(404)    

    q = 'SELECT albumid FROM Album WHERE albumid="%s"' % albumid_get

    db = connect_to_database()
    cur = db.cursor()
    cur.execute(q)
    results = cur.fetchall()
    if not results:
        print(404)
        abort(404)    


    #print(results)



    ## process POST
    target = os.path.join(APP_ROOT,'../static/images')
    if not os.path.isdir(target):
        os.mkdir(target)

    if request.method == 'POST':
        op = request.form["op"]
        print("GET POST, op:%s" % op)
        
        # if add POST
        if request.form["op"]=="add":

            op = request.form["op"]
            albumid = request.form["albumid"]

            print("[ GET ADD POST ] ")
            print("op: %s" % op)
            print("albumid: %s" % albumid)
            if 'file' not in request.files:
                #flash('No file part')
            	#return redirect(request.url)
                abort(404)
            file = request.files['file']
            if file.filename == "":
                #flash('No selected file')
                #return redirect(request.url)
            	return render_template("404.html",arg=albumid,reason='Enter Invalid Picture Name'), 404
            if not allowed_file(file.filename):
            	abort(404)
		#return render_template("404.html",arg=albumid,reason='Enter Invalid Picture Type'), 404
            #if file.filename == '':
            #    flash('No selected file')
            #    return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print("filename:%s, filetype: %s" % (filename,allowed_file(file.filename)))
                
                # save image
                #destination = "/".join([target,filename])
                m = hashlib.md5((str(albumid) + filename).encode('utf-8'))
                ext = filename.rsplit('.', 1)[1].lower()
                new_filename = m.hexdigest() + '.%s' % ext
                destination = "/".join([target,new_filename])
                print('image saved as: %s' % destination)
                file.save(destination)

                add_image_db(albumid,filename)

            return redirect(url_for('album.album_route',albumid=albumid))

        # if delete POST
        if request.form["op"]=="delete":

            op = request.form["op"]
            albumid = request.form["albumid"]
            picid = request.form["picid"]

            print("[ GET DELETE POST ]")
            print("op: %s" % op)
            print("albumid: %s" % albumid)
            print("picid: %s" % picid)

            delete_image_db(albumid,picid)

            



    picid_lst=get_picid_lst(albumid_get)
    #return render_template("album.html", **options, albumid=albumid_get, picid_lst=picid_lst)
    return render_template("album.html", edit=True, albumid=albumid_get, picid_lst=picid_lst)


@album.route('/album',methods=['GET','POST'])
def album_route():
    options = {
        "edit": False
    }

    ## get GET param
    albumid = request.args.get('albumid', '')
    print('albumid_route:%s' % albumid)

    # invalid case
    if not albumid:
        print(404)
        abort(404)

    q = 'SELECT albumid FROM Album WHERE albumid="%s"' % albumid

    db = connect_to_database()
    cur = db.cursor()
    cur.execute(q)
    results = cur.fetchall()
    if not results:
        print(404)
        abort(404)    

    # get Album info

    picid_lst=get_picid_lst(albumid)
    #return render_template("album.html", **options, albumid=albumid, picid_lst=picid_lst)
    return render_template("album.html", edit=False, albumid=albumid, picid_lst=picid_lst)

# test upload

@album.route('/add',methods=['GET','POST'])
def pic_add():
    options = {
        "albumid": 0
    }
    options['albumid'] = request.args.get('albumid', '')
    return render_template("upload.html",**options)

@album.route('/delete',methods=['GET','POST'])
def pic_delete():

    albumid = request.args.get('albumid', '')
    picid = request.args.get('picid', '')

    delete_image_db(albumid,picid)

    return redirect(url_for('album.album_route',albumid=albumid))

@album.route('/upload',methods=['GET','POST'])
def upload():
    options = {
        "albumid": 0
    }
    albumid = request.args.get('albumid', '')
    options['albumid'] = albumid
    print('albumid: %s' % albumid)

    target = os.path.join(APP_ROOT,'../static/images')

    if not os.path.isdir(target):
        os.mkdir(target)

    print('url',request.url)
    if request.method == 'POST':
        # check if the post request has the file part

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print("filename:%s, filetype: %s" % (filename,allowed_file(file.filename)))
            

            # save image
            #destination = "/".join([target,filename])
            m = hashlib.md5((str(albumid) + filename).encode('utf-8'))
            ext = filename.rsplit('.', 1)[1].lower()
            new_filename = m.hexdigest() + '.%s' % ext
            destination = "/".join([target,new_filename])
            print('image saved as: %s' % destination)
            file.save(destination)

            add_image_db(albumid,filename)

            return redirect(url_for('album.album_route',albumid=albumid))
    return ''

@album.route('/album/test',methods=['GET','POST'])
def album_test():

    if request.method == "POST":
        file = request.form['firstname']
        print(file)
        
    return render_template('index.html')
