from instaloader import instaloader
root = instaloader.Instaloader()
usr_name='pkhoddami'
print(root.download_profile(usr_name,profile_pic_only=True))