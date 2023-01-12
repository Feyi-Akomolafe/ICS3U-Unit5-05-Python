#!/usr/bin/env python3

# Created by: Feyi Akomolafe
# Created on: Dec 2022
# This program formats someones address using Canada Post format


def address(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):

    # return proper address

    proper = full_name + "\n"
    if apartment_number != None:
        proper = proper + str(apartment_number) + "-"
    proper = proper + str(street_number)
    proper = proper + " " + street_name + "\n"
    proper = proper + city + " "
    proper = proper + province + "  "
    proper = proper + postal_code

    return proper


def main():
    # main function
    apartment_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question == "y":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type (Pleasant prkw...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC...): ")
    postal_code = input("Enter your postal code (ABC 123): ")

    try:
        if apartment_number != None:
            apartment_number = int(apartment_number)
        street_number = int(street_number)
        proper_finish = address(
            full_name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )
        print("\n")
        print(proper_finish.upper())
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
