# Sales-Prediction-For-Pharmaceutical

This project is to forecast sales in all the stores across several cities six weeks ahead of time buy building and serving an end-to-end product that delivers this prediction to analysts in the finance team.

**Table of content**

- [Install](#install)
- [Data](#data)
- [Dashboard](#dashboard)
- [Notebooks](#notebooks)
- [Models](#models)
- [Scripts](#scripts)
- [Test](#test)
- [Authors](#authors)

## Introduction

The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales. As a Machine learning engineer, My job is to build and serve an end-to-end product that delivers this prediction to analysts in the finance team.

## Learning Outcomes

- Advanced use of scikit-learn
- Feature Engineering
- ML Model building and fine-tuning
- CI/CD deployment of ML models
- Python logging
- Unit testing
- Building dashboards
- Model management
- MLOps with DVC, CML, and MLFlow

## Install

```
git clone https://github.com/AntenehTilaye/Sales-Prediction-For-Pharmaceutical.git
cd Sales-Prediction-For-Pharmaceutical
pip install -r requirements.txt
```

## Data

The data for this challenge can be found [here at google drive](https://drive.google.com/file/d/1sGLyrytv6xYBrCPdjZkE1ZDSwngDij4W/view?usp=sharing). Or you can find it also here: [Rossmann Store Sales | Kaggle](https://www.kaggle.com/competitions/rossmann-store-sales/data)

Data fields

Most of the fields are self-explanatory. The following are descriptions for those that aren't.

- Id - an Id that represents a (Store, Date) duple within the test set
- Store - a unique Id for each store
- Sales - the turnover for any given day (this is what you are predicting)
- Customers - the number of customers on a given day
- Open - an indicator for whether the store was open: 0 = closed, 1 = open
- StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
- SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
- StoreType - differentiates between 4 different store models: a, b, c, d
- Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
- CompetitionDistance - distance in meters to the nearest competitor store
- CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
- Promo - indicates whether a store is running a promo on that day
- Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
- Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
- PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

## Dashboard

> All the scripts for creating dashboard can be found in the Dashboard folder.

## Notebooks

> All the EDA notebook file can be found in the notebooks folder.

## Models

> All the models generated will be found here in the models folder.
> All the databases schema will be found here in the models folder.

## Scripts

> All the Utils for Data munipulation and Ploting can be found here

## Tests

> All the unit and integration tests are found here in the tests folder.

## Author

👤 **Anteneh Tilaye**

- GitHub: [Anteneh Tilaye](https://github.com/AntenehTilaye)
- LinkedIn: [Anteneh Tilaye](https://www.linkedin.com/in/anteneh-tilaye-bb6770149/)
- Website: [Anteneh Tilaye Demo Porfolio](https://antenehtilaye.github.io/)

## Show ME your support

Give Me a ⭐ if you like this project!
