# Flex Unlimited #
## Automate searching and accepting Amazon Flex Driver jobs ##

Originally created by [mdesilva](https://github.com/mdesilva), this fork of Flex Unlimited aims to search for one given matching offer at a time, instead of searching until a request limit had been met. The optional twilio dependency has also been swapped for a free and open-source push notification system, so you can receive offer search push notifications right from your cell phone. Base functionality and verbosity has been altered to match a so-called 'dumb clicker;' difference being, this script is no-cost to the end user. After setting this up with a systemd job, you can achieve full automation if desired. Best results are achieved through connect-by-wire (or fiber) machines, keep in mind you are aiming for as low of latency to flex-capacity-na as possible.

## Usage ##

0. You MUST have python 3 installed. Versions below 3 will not work.  
1. Clone the repo to the machine you will be using to run the program (machine should be connected to Internet by wire for best results).
2. Install dependencies using **pip**: `pip install -r requirements.txt`.
3. Set `username` and `password` in **account.json**.
4. Modify **config.json** to meet your job search requirements. It already comes with some defaults. Fill out `desiredWarehouses` if you would like to restrict your job search to certain warehouses. If you choose this option, 
`desiredWarehouses` must be a list of strings of **internal warehouse ids**. Otherwise, leave `desiredWarehouses` as an empty list.
5. Fill out the `desiredWeekdays` filter in **config.json** if you would like to restrict your job search to certain days of the week. Otherwise, you may leave `desiredWeekdays` as an empty list. `desiredWeekdays` must be a list of strings (case insensitive) corresponding to days of the week (i.e. "Sun", "monday", etc.). Each string must include at least the first three letters of the day.

To determine the internal warehouse ids of warehouses you are eligible for, run the following command:
`python3 app.py getAllServiceAreas` OR `python3 app.py --w`

Here you will get a table of all the service areas (warehouses) that you are eligible for. The left column states the service area name, and the right column is the internal warehouse id used by Amazon. Copy all the service area ids you want to restrict your search to as strings into the **desiredWarehouses** field into the config.json. 

e.g
```
{
...
"desiredWarehouses": ["9c332725-c1be-405f-87c5-e7def58595f6", "5fa41ec8-44ae-4e91-8e48-7be008d72e8a"]],
...
}
```
5. Optionally, setup [ntfy.sh](https://ntfy.sh) notifications of Amazon Flex job acceptances by filling out the `ntfy` parameters in  **config.json**.
6. Run `python app.py`. Alternatively, try `python3 app.py`.

## Troubleshooting ##

- Unable to authenticate to Amazon Flex. Please try completing the two step verification challenge at (url)

Click on the url and complete the two step verification challenge. After you get to a page that says:

_Looking for Something?
We're sorry. The Web address you entered is not a functioning page on our site_

**You have successfully completed the two step verification challenge**. Go back to your terminal and re-run the program.



