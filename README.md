# PyMatchOrders

PyMatchOrders is a school project (Assignment 10) that will parse a csv file called orders.csv, located at the root of the project.
Then the scrip will match the orders from the sellers and the buyers and will display the ID of the matched trader is a deal is done.
If not it will add a 'REJECTED' at the end of the line.

## Installation

Python 3 is required in order to run this program  
Pipenv is required in order to run this program

### OSX

```bash
brew install python3
```

```bash
brew install pipenv
```

## Usage

In order to install the dependencies run :

```bash
pipenv install
```

Then to run the project use the following command:

```bash
pipenv run python pymatchorders.py
```


### Pipenv Shell

If you want to run the script with the pipenv shell, just use :

```bash
pipenv shell
```

Then:

```bash
python pymatchorders.py
```

If you have any trouble with pipenv use the help flag:

```bash
pipenv --help
```


## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)