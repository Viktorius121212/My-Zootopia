import json
import data_fetcher


def serialize_animal(animal):
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal.get("name")}</div>\n'
    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    diet = characteristics.get("diet")
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'

    locations = animal.get("locations")
    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

    animal_type = characteristics.get("type")
    if animal_type:
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    output_string = ""

    if len(animals_data) == 0:
        output_string = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
    else:
        for animal in animals_data:
            output_string += serialize_animal(animal)

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output_string)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)


if __name__ == "__main__":
    main()

