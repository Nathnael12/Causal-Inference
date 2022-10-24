![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)
# Causal-Inference
## Logistic optimization: Delivery drivers location optimization with Causal Inference 

<br/>

> ### If we were to collect observations of a cockerel crowing and the sun rising there would certainly be a correlation but the knowledge that the cockerel's crows does not cause the sun to rise could not be intuited from the data alone.
___
<br/>


Our client is Gokada. Gokada is the largest last mile delivery service in Nigeria. Its works are partnered with motorbike owners and drivers to deliver parcels across Lagos, Nigeria.

The inefficient positioning of pilots (Gokada refers to its motor drivers as pilots) and customers who wish to utilize Gokada to ship their parcel is one of the major problems the company has encountered (as it grows its business). This has caused many delivery orders to be unmet.

We will work on Gokada’s data to understand the primary causes of unfulfilled requests as well as come up with solutions that recommend drivers locations that increase the fraction of complete orders. Since drivers are paid based on the number of requests they accept, the solution
(we’ll eventually propose) will help Gokada business grow both in terms of client satisfaction and increased business.

We will try to answer some interesting question that cannot be answered by just analyzing observational data alone.

**These questions can be similar to:**

• Given drivers are recommended to move 1km every 30 mins in a selected direction, what happens to the number of unfulfilled requests?

• If we assume we know the location of the next 20% of orders within 5km accuracy, what happens to the number of unfulfilled requests?

• Had we changed the time requirements to drivers operating time in the past, what fractions of orders could have been completed?

• If I increased the number of drivers by 10% cumulative per month, what fraction of orders can be completed?

# Folder Structure

## notebooks
Here you will find three separate notebooks for the following purposes
- EDA for dataset 1 (Information about compoleted orders)
- EDA for dataset 2 (Information about drivers at the time of request)
- Causal Inference and Causal Graphs

## Some screenshots from the EDA
Locations of origin for requests
![](./doc/map%20I.png)

Locations of destination for requests
![](./doc/map%20II.png)

## scripts
Here you will find methods and functions to ease your data cleaning and data extraction task

## tests
unit tests for the methods found in scripts directory

# Instalation

```bash

git clone https://github.com/Nathnael12/Causal-Inference.git
cd Causal-Inference
pip install -r requirements.txt

```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)