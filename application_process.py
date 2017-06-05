import psycopg2


def main():
    while True:
        print_menu()
        selected_menu_point = select_menu()
        user_query = selected_query(selected_menu_point)
        query_result = return_query_result(user_query)
        print(query_result)


def print_menu():
    menu_list = [
        "1: Mentors first and last name",
        "2: Mentors nick name, from Miskolc",
        "3: Carols full name",
        "4: Girl from Adipiscingenimmi University",
        "5: Insert the new guy, show the new guy\'s data",
        "6: UPDATE Jemima Forman",
        "7: Delete guys, from mauriseu.net"
    ]

    for line in menu_list:
        print(line)


def select_menu():
    choice = int(input('Please choose a query and press a number from 1 to 7: '))
    if choice >= 1 and choice <= 7:
        return choice
    else:
        return select_menu()


def selected_query(user_choice_menu_number):
    query_list = [
        "SELECT first_name, last_name FROM mentors;",
        "SELECT nick_name FROM mentors WHERE city = \'Miskolc\';",
        "SELECT CONCAT(first_name, \' \', last_name) AS full_name FROM applicants WHERE first_name = \'Carol\';",
        "SELECT CONCAT(first_name, \' \', last_name) AS full_name, phone_number FROM applicants WHERE email LIKE \'%@adipiscingenimmi.edu\';",
        "INSERT INTO applicants VALUES (11, \'Markus\', \'Schaffarzyk\', \'003620/725-2666\', \'djnovus@groovecoverage.com\', 54823);\nSELECT * FROM applicants WHERE application_code = 54823;",
        "UPDATE applicants SET phone_number=\'003670/223-7459\' WHERE fisrt_name = \'Jemima\' AND last_name = \'Foreman\';",
        "DELETE * FROM applicants WHERE email LIKE \'%mauriseu.net\';"
    ]
    return query_list[user_choice_menu_number-1]


def return_query_result(query):
    connect_str = "dbname='tovics' user='tovics' host='localhost' password='88Szekér99'"
    connection = psycopg2.connect(connect_str)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


if __name__ == '__main__':
    main()
