import boto3
import sys
import time

production_jar_service_option_settings = """
[
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "InstancePort",
        "Value": "80"
        },

     {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "InstancePort",
        "Value": "443"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "InstanceType",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application:environment",
        "OptionName": "JDBC_CONNECTION_STRING",
        "Value": ""
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Interval",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "5"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Timeout",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "4"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "UnhealthyThreshold",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "5"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "Stickiness Policy",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "false"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Target",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "Stickiness Cookie Expiration",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "0"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "LoadBalancerPorts",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": ":all"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "HealthyThreshold",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "3"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application",
        "OptionName": "Application Healthcheck URL",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "ELBScheme",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "public"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "VPCId",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "Subnets",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "AssociatePublicIpAddress",
        "Value": "true"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "InstanceProtocol",
        "Value": "HTTPS"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "ListenerEnabled",
        "Value": "true"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "ListenerProtocol",
        "Value": "HTTPS"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "InstancePort",
        "Value": "443"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "SSLCertificateId",
        "Value": "arn:aws:iam::834337284708:server-certificate/CERTIFICATE"
        },
    {
        "Namespace": "aws:elb:loadbalancer",
        "OptionName" : "CrossZone",
        "Value" : "true"
        },
    {
        "Namespace": "aws:elb:loadbalancer",
        "OptionName" : "LoadBalancerHTTPSPort",
        "Value" : "443"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "IamInstanceProfile",
        "Value": "aws-elasticbeanstalk-ec2-role"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "MonitoringInterval",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "5 minute"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "SecurityGroups",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "%s"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "SSHSourceRestriction",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "tcp, 22, 22, 50.18.61.184/32"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "EC2KeyName",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "%s_ec2"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MaxSize",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Cooldown",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "300"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MinSize",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Availability Zones",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "Any 2"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "UpperThreshold",
        "ResourceName": "AWSEBCloudwatchAlarmHigh",
        "Value": "70"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Period",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "5"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Statistic",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "Average"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "MeasureName",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "CPUUtilization"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "LowerThreshold",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "20"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "EvaluationPeriods",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Unit",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "Percent"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "BreachDuration",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "5"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "LowerBreachScaleIncrement",
        "ResourceName": "AWSEBAutoScalingScaleDownPolicy",
        "Value": "-1"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "UpperBreachScaleIncrement",
        "ResourceName": "AWSEBAutoScalingScaleUpPolicy",
        "Value": "1"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "RollbackLaunchOnFailure",
        "Value": "false"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "DefaultSSHPort",

        "Value": "22"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "AssociatePublicIpAddress",
        "Value": "true"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "LaunchType",
        "Value": "Normal"
        },
    {
        "Namespace": "aws:elasticbeanstalk:monitoring",
        "OptionName": "Automatically Terminate Unhealthy Instances",
        "Value": "true"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "LaunchTimeout",
        "Value": "0"
        },
    {
        "Namespace": "aws:elasticbeanstalk:sns:topics",
        "OptionName": "Notification Endpoint",
        "Value": "devops@COMPANY.com"
        },
    {
        "Namespace": "aws:elasticbeanstalk:sns:topics",
        "OptionName": "Notification Protocol",
        "Value": "email"
        }
]"""


production_service_option_settings = """
[
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "Xmx",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "JVM Options",
        "Value": "%s"
        },
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "JVMOptions",
        "Value": "%s"
        },
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "InstancePort",
        "Value": "80"
        },
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "InstancePort",
        "Value": "443"
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "XX:MaxPermSize",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "Xms",
        "Value": "%s"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "InstanceType",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application:environment",
        "OptionName": "JDBC_CONNECTION_STRING",
        "Value": ""
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Interval",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "5"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Timeout",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "4"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "UnhealthyThreshold",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "5"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "Stickiness Policy",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "false"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Target",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "Stickiness Cookie Expiration",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "0"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "LoadBalancerPorts",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": ":all"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "HealthyThreshold",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "3"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application",
        "OptionName": "Application Healthcheck URL",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "ELBScheme",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "public"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "VPCId",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "Subnets",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "AssociatePublicIpAddress",
        "Value": "true"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "InstanceProtocol",
        "Value": "HTTPS"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "ListenerEnabled",
        "Value": "true"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "ListenerProtocol",
        "Value": "HTTPS"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "InstancePort",
        "Value": "443"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "SSLCertificateId",
        "Value": "arn:aws:iam::834337284708:server-certificate/CERTIFICATE"
        },
    {
        "Namespace": "aws:elb:loadbalancer",
        "OptionName" : "CrossZone",
        "Value" : "true"
        },
    {
        "Namespace": "aws:elb:loadbalancer",
        "OptionName" : "LoadBalancerHTTPSPort",
        "Value" : "443"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "IamInstanceProfile",
        "Value": "aws-elasticbeanstalk-ec2-role"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "MonitoringInterval",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "5 minute"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "SecurityGroups",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "%s"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "SSHSourceRestriction",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "tcp, 22, 22, 50.18.61.184/32"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "EC2KeyName",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "%s_ec2"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MaxSize",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Cooldown",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "300"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MinSize",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Availability Zones",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "Any 2"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "UpperThreshold",
        "ResourceName": "AWSEBCloudwatchAlarmHigh",
        "Value": "40"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Period",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "5"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Statistic",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "Average"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "MeasureName",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "CPUUtilization"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "LowerThreshold",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "20"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "EvaluationPeriods",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Unit",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "Percent"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "BreachDuration",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "5"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "LowerBreachScaleIncrement",
        "ResourceName": "AWSEBAutoScalingScaleDownPolicy",
        "Value": "-1"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "UpperBreachScaleIncrement",
        "ResourceName": "AWSEBAutoScalingScaleUpPolicy",
        "Value": "1"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "RollbackLaunchOnFailure",
        "Value": "false"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "DefaultSSHPort",

        "Value": "22"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "AssociatePublicIpAddress",
        "Value": "true"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "LaunchType",
        "Value": "Normal"
        },
    {
        "Namespace": "aws:elasticbeanstalk:monitoring",
        "OptionName": "Automatically Terminate Unhealthy Instances",
        "Value": "true"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "LaunchTimeout",
        "Value": "0"
        },
    {
        "Namespace": "aws:elasticbeanstalk:sns:topics",
        "OptionName": "Notification Endpoint",
        "Value": "devops@COMPANY.com"
        },
    {
        "Namespace": "aws:elasticbeanstalk:sns:topics",
        "OptionName": "Notification Protocol",
        "Value": "email"
        }
]"""


production_stalk_option_settings = """
[
    {
        "Namespace": "aws:elasticbeanstalk:application:environment",
        "OptionName": "AWS_SECRET_KEY",
        "Value": ""
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "Xmx",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application:environment",
        "OptionName": "AWS_ACCESS_KEY_ID",
        "Value": ""
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "JVM Options",
        "Value": "%s"
        },
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "JVMOptions",
        "Value": "%s"
        },
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "InstancePort",
        "Value": "80"
        },
    {
        "Namespace": "aws:cloudformation:template:parameter",
        "OptionName": "InstancePort",
        "Value": "443"
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "XX:MaxPermSize",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:container:tomcat:jvmoptions",
        "OptionName": "Xms",
        "Value": "%s"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "InstanceType",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application:environment",
        "OptionName": "JDBC_CONNECTION_STRING",
        "Value": ""
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Interval",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "5"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Timeout",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "4"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "UnhealthyThreshold",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "5"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "Stickiness Policy",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "false"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "Target",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "Stickiness Cookie Expiration",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "0"
        },
    {
        "Namespace": "aws:elb:policies",
        "OptionName": "LoadBalancerPorts",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": ":all"
        },
    {
        "Namespace": "aws:elb:healthcheck",
        "OptionName": "HealthyThreshold",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "3"
        },
    {
        "Namespace": "aws:elasticbeanstalk:application",
        "OptionName": "Application Healthcheck URL",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "ELBScheme",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "public"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "VPCId",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "Subnets",
        "ResourceName": "AWSEBLoadBalancer",
        "Value": "%s"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "AssociatePublicIpAddress",
        "Value": "true"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "InstanceProtocol",
        "Value": "HTTPS"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "ListenerEnabled",
        "Value": "true"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "ListenerProtocol",
        "Value": "HTTPS"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "InstancePort",
        "Value": "443"
        },
    {
        "Namespace": "aws:elb:listener",
        "OptionName": "SSLCertificateId",
        "Value": "arn:aws:iam::834337284708:server-certificate/CERTIFICATE"
        },
    {
        "Namespace": "aws:elb:loadbalancer",
        "OptionName" : "CrossZone",
        "Value" : "true"
        },
    {
        "Namespace": "aws:elb:loadbalancer",
        "OptionName" : "LoadBalancerHTTPSPort",
        "Value" : "443"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "IamInstanceProfile",
        "Value": "aws-elasticbeanstalk-ec2-role"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "MonitoringInterval",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "5 minute"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "SecurityGroups",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "%s"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "SSHSourceRestriction",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "tcp, 22, 22, 50.18.61.184/32"
        },
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "EC2KeyName",
        "ResourceName": "AWSEBAutoScalingLaunchConfiguration",
        "Value": "%s_ec2"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MaxSize",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Cooldown",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "300"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MinSize",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Availability Zones",
        "ResourceName": "AWSEBAutoScalingGroup",
        "Value": "Any 2"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "UpperThreshold",
        "ResourceName": "AWSEBCloudwatchAlarmHigh",
        "Value": "40"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Period",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "5"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Statistic",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "Average"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "MeasureName",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "CPUUtilization"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "LowerThreshold",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "20"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "EvaluationPeriods",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "1"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "Unit",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "Percent"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "BreachDuration",
        "ResourceName": "AWSEBCloudwatchAlarmLow",
        "Value": "5"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "LowerBreachScaleIncrement",
        "ResourceName": "AWSEBAutoScalingScaleDownPolicy",
        "Value": "-1"
        },
    {
        "Namespace": "aws:autoscaling:trigger",
        "OptionName": "UpperBreachScaleIncrement",
        "ResourceName": "AWSEBAutoScalingScaleUpPolicy",
        "Value": "1"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "RollbackLaunchOnFailure",
        "Value": "false"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "DefaultSSHPort",

        "Value": "22"
        },
    {
        "Namespace": "aws:ec2:vpc",
        "OptionName": "AssociatePublicIpAddress",
        "Value": "true"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "LaunchType",
        "Value": "Normal"
        },
    {
        "Namespace": "aws:elasticbeanstalk:monitoring",
        "OptionName": "Automatically Terminate Unhealthy Instances",
        "Value": "true"
        },
    {
        "Namespace": "aws:elasticbeanstalk:control",
        "OptionName": "LaunchTimeout",
        "Value": "0"
        },
    {
        "Namespace": "aws:elasticbeanstalk:sns:topics",
        "OptionName": "Notification Endpoint",
        "Value": "devops@COMPANY.com"
        },
    {
        "Namespace": "aws:elasticbeanstalk:sns:topics",
        "OptionName": "Notification Protocol",
        "Value": "email"
        }
]"""

solution_name = "64bit Amazon Linux 2016.03 v2.1.1 running Tomcat 7 Java 7"

def get_ebstalk_connection(region):
    conn = boto3.client('elasticbeanstalk', region_name=region)
    return conn

def create_new_application(conn, app_name, desc):
    status = conn.create_application(ApplicationName=app_name, Description=desc)
    return status

def create_new_environment(conn, options):
    status = conn.create_environment(
        ApplicationName=options['appname'],
        EnvironmentName=options['hostname'],
        CNAMEPrefix=options['envname'],
        Tags=[
            {
                'Key': 'Name',
                'Value': options['hostname']
                },
            ],
        SolutionStackName=options['solutionstack'],
        OptionSettings=options['settings'][0],
        )
    return status

def get_ebstalk_environments(conn):
    environments = conn.describe_environments()
    return environments

def get_ebstalk_resources(conn, envname):
    status = conn.describe_environment_resources(EnvironmentName=envname)
    return status

def get_ebstalk_elb_name(conn, envname):
    status = get_ebstalk_resources(conn, envname)
    print status
    return status['EnvironmentResources']['LoadBalancers'][0]['Name']

def get_ebstalk_instance_ids(conn, envname):
    status = get_ebstalk_resources(conn, envname)
    return status['EnvironmentResources']['Instances']

def is_ebstalk_ready(conn, envname):
    time.sleep(10)
    status = conn.describe_environments(EnvironmentNames=[envname,])
    try:
        #print status['Environments'][0]
        if status['Environments'][0]['Health'] != 'Grey' and status['Environments'][0]['Status'] != 'Launching':
            return True
        else:
            return False
    except:
        return False

