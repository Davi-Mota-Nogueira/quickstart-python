from cassandra.cluster import Cluster

def create_connection():
    cluster = Cluster()
    return cluster.connect('demo')

def set_user(session, lastname, age, city, email, firstname):
    session.execute("INSERT INTO users (lastname, age, city, email, firstname) VALUES (%s,%s,%s,%s,%s)", [lastname, age, city, email, firstname])


def get_user(session, lastname):
    rows = session.execute("SELECT * FROM users WHERE lastname = %s", [lastname])
    for user_row in rows:
        print user_row.firstname, user_row.age

def update_user(session, new_age, lastname):
    session.execute("UPDATE users SET age =%s WHERE lastname = %s", [new_age, lastname])

def delete_user(session, lastname):
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
