# Perfio

## What we do here
A performance IO tool to measure and benchmark sanity tests on HDD, SDD, and RAID.

## How to run
I've worked hard to make the program portable. Only requirement is python3 which is installed in every major linux distribution.
Just run the `perfio` executable with valid parameters. Make sure that the program has valid execution permissions.
If it doesn't, run `chmod +x ./perfio`


## Usage
### Navigating the menu
Once the application starts you can use the `<up>`, `<down>`, `<left>`, `<right>` keys to navigate through the application.
Once your cursor is in the desired option, press `<enter>` to execute/enter.
Press `<space>` to select / unselect a checkbox
First, we will see a menu with options.

## Create test
Making a test is required, this will create a configuration file with instructions on how to execute the test. 
This step is not essential as we can re-use test for different scenarios.


### Test creation
To create a test we have to select the devices that we want to test first.


## Run previous test
In the case test instructions have already been made, we can use the generated file to re-run the test with ease.