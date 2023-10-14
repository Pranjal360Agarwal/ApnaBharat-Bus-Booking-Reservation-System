# user_profile.py
import sqlite3

def get_user_profile(username):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user_profile = cursor.fetchone()
    
    conn.close()
    return user_profile

def update_user_profile(username, new_email, new_contact_number):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE users SET email=?, contact_number=? WHERE username=?", (new_email, new_contact_number, username))
    conn.commit()
    conn.close()
    return "Profile updated successfully."

# Usage
username = "user123"
user_profile = get_user_profile(username)
print("User Profile:")
print(user_profile)

# Update User Profile
new_email = "newemail@example.com"
new_contact_number = "123-456-7890"
update_result = update_user_profile(username, new_email, new_contact_number)
print(update_result)
