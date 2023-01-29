

def get_home_town() -> str:
    print('What is your home town?')
    home_town = input()
    return home_town


def get_pet_name() -> str:
    print("What is/was your pet's name?")
    pet_name = input()
    return pet_name


def generate_band_name(home_town: str, pet_name: str) -> str:
    band_name = f"The {home_town} {pet_name}"
    return band_name


def output_band_name(band_name: str):
    print(f"Hmm, a good name for your band could be {band_name}")


def execute():
    home_town = get_home_town()
    pet_name = get_pet_name()
    band_name = generate_band_name(home_town, pet_name)
    output_band_name(band_name)


if __name__ == '__main__':
    execute()
