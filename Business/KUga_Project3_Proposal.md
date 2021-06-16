## Predictive Maintenance for Mechanical Components

Kalu Chibueze Uga

#### Abstract
Mechanical failure is a part of all components and it could have severe consequences like loss of revenue or loss of human life. The ability to correctly predict when a component is likely to fail will help companies improve utilization of parts and avoid unnecessary downtime due to component failure. The goal of this project is to show that using historic dataset which shows point of failure, we can predict when a component will likely fail in the future so that replacements can be scheduled before failure or components can be taken out of service before their breaking point.

#### Design
* The end goal of this project is to reduce loss of revenue from component failure. We will utilize components until they need to be serviced of replaced. We can reduce overhead cost by allocating the correct number of personels to service components that need attention based on demand. Ultimately, we can keep our clients happy and retain contracts by reducing component breakdown through predictive maintenance. This approach will boost revenue in the long term.
* The solution path will use historic heath data to create a classification for components that are likely to fail within the next 30 days or to predict the remaining useful life of the component by using regression.
* A measure of success will be to correctly predict 70 percent of failures before they happen.
* Given that the model will be tested on a training set, we run the risk of drawing wrong conclusion if we get poor quality data from real time operation, thus leading to wrong predictions. 
* It is assumed that third party sensors are operating as expected and the sensor readings are correct. Components that fail right after deployment will contibute to outliers in the model.

#### Data 
The dataset will be NASA TurboFan Engine data provided by NASA. 

#### Tools
* Google spreadsheet will be used for cleaning the data and performing exploratory data analysis.
* Tableau will be used to create an interactive dashboard for data visualization.

#### MVP Goal
The goal of this project is to show that using historic health data of components, we can plan ahead by classifying components that are likely to break and to correctly predict future breaking point so that replacement could be scheduled before the component reaches its breaking point.