from cassandra.cluster import Cluster

def create_connection():
    # TO DO: Fill in your own contact point
    cluster = Cluster(['127.0.0.1'])
    return cluster.connect('demo')

def set_user(session, lastname, age, city, email, firstname):
     # TO DO: execute SimpleStatement that inserts one user into the table
    session.execute("INSERT INTO users (lastname, age, city, email, firstname) VALUES (%s,%s,%s,%s,%s)", [lastname, age, city, email, firstname])

def get_user(session, lastname):
    # TO DO: execute SimpleStatement that retrieves one user from the table
    # TO DO: print firstname and age of user
    result = session.execute("SELECT * FROM users WHERE lastname = %s", [lastname]).one()
    print result.firstname, result.age

def update_user(session, new_age, lastname):
    # TO DO: execute SimpleStatement that updates the age of one user
    session.execute("UPDATE users SET age =%s WHERE lastname = %s", [new_age, lastname])

def delete_user(session, lastname):
    # TO DO: execute SimpleStatement that deletes one user from the table
    session.execute("DELETE FROM users WHERE lastname = %s", [lastname])


def main():

    session = create_connection()
    lastname = "Jones"
    age = 35
    city = "Austin"
    email = "bob@example.com"
    firstname = "Bob"
    new_age = 36

    set_user(session, lastname, age, city, email, firstname)

    get_user(session, lastname)

    update_user(session, new_age, lastname)

    get_user(session, lastname)

    delete_user(session, lastname)

if __name__ == "__main__":
    main()
