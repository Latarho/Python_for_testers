Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <first_name>, <last_name> and <mobile>
    When I add the contact to the list
    Then The new contact list is equal to the old list with the added contact

    Examples:
    | first_name  | last_name  | mobile  |
    | first_name1 | last_name1 | mobile1 |
    | first_name2 | last_name2 | mobile2 |

Scenario: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I modify a contact from the list
    Then the new list is equal to the old list with modified contact

Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete a contact from the list
    Then the new list is equal to the old list without the deleted contact