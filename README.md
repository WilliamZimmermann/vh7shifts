# vh7shifts
VanHack Fair. App for 7 shifts.

`# Project Title

7Shifts Timetracker

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
The system was developed using Python 3.* + Django 2.*. I'm using SQLite to retain all data provided by the JSON API. Since tests are important, take a look in the main point "Testing" to know how to do it.

### Prerequisites

Download and Install Python 3.* (https://www.python.org/)
Install pip
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py


### Installing

Next, go to the project path and type
$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages


## Testing

Just type in your terminal:
$ python manage.py test

You will tests running and, if something goes wrong, you will clearly see what happens.

## Deployment

To run this project in your browser, open your project in the terminal and type:
$ python manage.py runserver

If all it's ok, it will give you the follow:
Performing system checks...

System check identified no issues (0 silenced).
June 23, 2018 - 20:36:15
Django version 2.0.6, using settings 'pyvh7s.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Just type the address that Python and Vagrant gives you.

## Built With

* [Django](https://www.python.org/) - The web framework used
* [Pip](https://pip.pypa.io/en/stable/installing/) - Dependency Management


## Versioning

We use [GitHub](http://github.com/) for versioning. Please, use the release/0.2.0 to test as the system is not completed yet.

## Authors

* **William Zimmermann** - [Blog](http://www.williamzimmermann.com.br)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

`
