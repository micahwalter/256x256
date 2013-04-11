from PIL import Image
import sys, os
from random import randint
import json
import boto
from datetime import datetime
import cStringIO

s3_key = os.environ['S3_KEY']
s3_secret = os.environ['S3_SECRET']
s3_bucket = os.environ['S3_BUCKET']

def randomImage():
	size = 256,256
	im = Image.new("L", size)

	for w in range(256):
		for h in range(256):
			im.putpixel((w,h), randint(0,256))
	
	out_im = cStringIO.StringIO()
	im.save(out_im, 'PNG')
	
	conn = boto.connect_s3(s3_key, s3_secret)
	bucket = conn.create_bucket(s3_bucket)
	from boto.s3.key import Key
	k = Key(bucket)
	k.key = datetime.now().strftime('%Y-%m-%d-%H%M%S')+".png"
	k.set_metadata('Content-Type','image/png')
	k.set_contents_from_string(out_im.getvalue())
	k.set_acl('public-read')
	
	
	rsp = {}
	rsp = {'url': "https://s3.amazonaws.com/"+s3_bucket+"/"+k.key, 'status': "ok"}
	rsp = json.dumps(rsp)

	return rsp