
class message:
    def __init__(self,message):
        self.msg=message
    def get_msg_id:
        #To return the id of this message
        return self.msg['SmsMessageSid']
    def get_frm(self):
        #to return the number for the user who sent the messsage
        return self.msg['From']
    def get_body(self):
        #To return the body of this message
        return self.msg['Body']
    def get_num_of_media(self):
        #to get the number of media sent
        return self.msg['NumMedia']
    def get_content_media_type(self):
        #To return the media content type associated with this message
        return self.msg['MediaContentType0']
    def get_media_url(self):
        #To return the media url associated with this message, this is not only null if the
        #message is  sent with a media e.g a picture
        return self.msg['MediaUrl0']