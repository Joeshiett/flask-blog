# Flask Blog
![](images/flaskblog.png)
# Introduction
This FlaskBlog web application is simply built with the micro-web framework **Flask**, HTML and the CSS framework **Bootstrap**. Different features in this application such as user authentication and password reset via email was all made possible with the aid of the available functionalities in flask such as Flask-WTF, Flask-Login, Flask-Mail etc.

# Deployment
The web application has been deployed on AWS to EC2 instances set up in an autoscaling group in different AZs (Availability Zones), with an Elastic Load Balancer attached to a target group containing the EC2 instances. Here is the URL to access the web application [link](https://joeshiett.xyz). 

![](images/FlaskblogAwsArchitecture.png)

### Before each EC2 instance was created and configured to serve the web application:
- An **AMI image** was created. This AMI image contains the dependencies that the Flask application would require. Such as Nginx, Gunicorn etc.

- A **launch template** was created as well specifying the type of instances to be created and deployed using the AMI image created above.
- An **autoscaling group** was created with the launch template included. 

- A **security group** was created in the default VPC. Different ports were exposed to allow access for the different protocols (HTTP, TCP and HTTPS).

- A **target group** was created and the two instances created with the launch template were included in the **registered templates**.

- An **Application Load Balancer** was created and linked to the target group and the **listeners** for each protocol (HTTP and HTTPS) were setup with the necessary **security policy** and **SSL certificate**.

- A free **public SSL certificate** was acquired from the ACM (Amazon Certificate Manager).

- A domain name was acquired from **Namecheap** and added to Hosted Zones in **Route 53**. 

- Custom Domain Name Servers were created on Namecheap and the AWS NS record was copied and added as part of the Custom Domain Name Servers.

- **CNAME** records and **A** records were created on Route 53 for proper routing to the purchased domain.