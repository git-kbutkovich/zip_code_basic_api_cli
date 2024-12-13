from argparse import ArgumentParser

import click

# import requests
import psycopg2

# TODO: get argument parser working properly with the CLI call.

@click.group()
def cli():
    pass


# class ArgumentParser(argparse.ArgumentParser):
#     # Argparser doesn't return an exception, so report the error from here. This is
#     # required to catch if a template job fails to launch due to an invalid argument
#     # that's passed from the cloud function (that launches these jobs)
#     # Source: https://stackoverflow.com/a/5943389/7543727
#     def error(self, message: str) -> NoReturn:  # pragma: nocover
#         self.print_help(sys.stderr)

#         client = error_reporting.Client(service=SERVICE_NAME)
#         client.report(f"ArgumentParserError: {self.prog}: {message}")

#         self.exit(2, "%s: error: %s\n" % (self.prog, message))

# @click.command()
# @click.option('--zip-code', required=True, help = "the zip code")
# @click.option('--method', default='GET', help='The HTTP method to use.')
# # @click.option('--data', help='JSON data to send with the request.')
# def main(zip_code):
#     click.echo(f"zip_code: {zip_code}")


def postgres_connection():
    p_db_name = "postgres"
    p_user = "postgres"
    p_pass = ""
    port = '5433'

    conn = psycopg2.connect(database=p_db_name, user=p_user, password=p_pass, host="localhost", port=port)
    cursor = conn.cursor()
    return cursor


@click.command()
@click.option("--zip_code", "-zc", required=True)
def fetch_data(zip_code):
    click.echo(zip_code)
    cursor = postgres_connection()
    print("cursor fetched")

    sql = f"select * from zip_codes WHERE zip_code = '{zip_code}';"

    cursor.execute(sql)
    result = cursor.fetchone()
    print({"zip_code": f"{result[2]}", "city": f"{result[3]}", "state": f"{result[5]}"})


# def get_zip_code_info(zip_code):
#     """Fetch zip code info."""

#     if method == 'GET':
#         response = requests.get(endpoint)
#     elif method == 'POST':
#         response = requests.post(endpoint, json=data)
#     # Add more methods as needed (PUT, DELETE, etc.)

#     if response.status_code == 200:
#         click.echo(response.json())
#     else:
#         click.echo(f"Error: {response.status_code}")


def main():
    try:
        #     # fetch_data('80122')
        parser = ArgumentParser()
        parser.add_argument("zip_code")
        #     # parser.add_argument("--city", default=None)
        args = parser.parse_args()
        print("Args: ", args)

        fetch_data(args.zip_code)

    #     # main(**vars(known_args), pipeline_args=pipeline_args)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":  # pragma: nocover
    cli.add_command(fetch_data)
    cli()
