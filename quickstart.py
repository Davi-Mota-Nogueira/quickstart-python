from cassandra.cluster import Cluster

def create_connection():
    # TO DO: Fill in your own contact point
    cluster = Cluster(['127.0.0.1'])
    return cluster.connect('demo')

def set_user(session, lastname, age, city, email, firstname):
    # TO DO: execute SimpleStatement that inserts one user into the table


def get_user(session, lastname):
    # TO DO: execute SimpleStatement that retrieves one user from the table
    # TO DO: print firstname and age of user


def update_user(session, new_age, lastname):
    # TO DO: execute SimpleStatement that updates the age of one user


def delete_user(session, lastname):
    # TO DO: execute SimpleStatement that deletes one user from the table


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
