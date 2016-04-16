# Overview

This repository contains the file process code, its unittest code, performace testing methods and other testing methods. Beyond the implementation, I think more for a real product. This code has limitations for file content process, large file process, muticore or distribution calculation and testing framework for central manage testing scripts. So, I'm not just descprit what I implemented with but also it will with.<br>

[![Build Status](https://travis-ci.org/i070595/emc1.svg?branch=master)](https://travis-ci.org/i070595/emc1)
<br>

# Description

This program is composed by three parts: file check, sum calculation and count calculation. The file check part is used to validate the file path, file content and file size. If there are some content that are not blank space or number, the file check function should kickoff such content. When a file size is too big to process by a machine, file check function should chunk the file and distribute the chunked file to different CPU core for processing or distribute it to a cluster for distribution processing.  When we start to sum or count a file, we need to pay attention to the calculation performance, result precision and hardware requirements. <br>
<br>
Based on above requirements, we need to have testing from below aspects:
<br>

## Unit testing
The unittest should cover more than 90%, the coverage can be detected by coveralls. And unittest covered the “CheckFile”, “SumFile” and “CountFile”.  This is used to protect our program from changes and regression.
<br><br>

## Function testing
Function test focuses on product feature testing. During feature development, function testing majorly depends on manually testing and run sanity automation testing to find regression bugs. When the feature development finished, we should delivery test case and automation testing script. <br>
<br>
Function’s automation testing script is majorly implemented on the UI part or Backend Service part. If our product’s architecture was B/S mode, the Selenium Webdriver + Python will be the base framework for our function testing from UI. If our product’s services were exposed as Restful web service, we can use Jmeter to simulate the HTTP requests and parse and assert the response data.<br>
<br>

## Performance testing
Introduce “cProfile” to do the performance analysis.  It will identify the times a function called, function total runtime, function average run time, function cumulated run time and function cumulated average run time. It will be very helpful to find the hot point of a program.<br>
<br>
Introduce “memorty_profile” to do the memory usage analysis. It will list the each line memory usage and memory increment. It will be very helpful to track memory leak, analysis memory usage and optimize the program algorithm.<br>
<br>
From end to end performance testing, we can introduce Jmeter if it is exposed as Webservice. We can simulate multiple users to request the resource in a specific time slot, for example, test the response time for 100 users request the resource in 10 seconds.<br>
<br>

## Integration testing
Integrate this program with the system, check whether it is work correct when there are services dependencies. This is rely on the integration environment and end to end business scenarios. In this case, the end to end scenarios is: 
* Input a file_path
* Validate the file_path
* Sum the numbers in the file
* Count the numbers in the file
* Output the calculation results
<br><br>
On each steps, we set a checkpoint and verify the result. The testing report will be collected by Testing Center and send to stakeholders<br>
<br>

## How to run
    pip install -r requirements.txt
    python processfile.py <data_file_path>

