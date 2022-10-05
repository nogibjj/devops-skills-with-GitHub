[![CI](https://github.com/nogibjj/devops-skills-with-GitHub/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/devops-skills-with-GitHub/actions/workflows/main.yml)
[![Codespaces Prebuilds](https://github.com/nogibjj/devops-skills-with-GitHub/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/nogibjj/devops-skills-with-GitHub/actions/workflows/codespaces/create_codespaces_prebuilds)

[![codebuild](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiWU15MDBDcTUxYkR4elUzZkh1ZlVLQWEyaVBCWGxGN3lqci91RWhIa0dhdyt5TmN5SXo1eVVoMTNDT1k4cTIzV3Q1bC9FWk14VHgwRVBGdVdVMEJVcU9BPSIsIml2UGFyYW1ldGVyU3BlYyI6IkYzR09TY0swZnR1dUltSmwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

# devops-skills-with-GitHub
All of the tools for building devops workflows

## Part2:  Automating Text and Filesystem

* dive into pathlib

## Part 3:  Build containerized Microservice
/docs get to swagger

![fastapi](https://user-images.githubusercontent.com/58792/192342466-e043cce7-c4f4-4811-9d0c-68fb884daadf.png)

#change

## Docker

`docker build .`
`docker image ls` #find image
`docker run -p 127.0.0.1:8080:8080 93fa55efa692` <replace with your image>

### Cloud9 + ECR + App Runner

  ![continuous-delivery](https://user-images.githubusercontent.com/58792/192845522-09207ae8-0dfb-4d31-b0a3-d396765d0db7.png)

  
  
* Clone repo into Cloud9 (pick a machine with decent size CPU and RAM if possible, but students should use micro)
* Add ssh keys to GitHub
* [resize to bigger disk](https://gist.github.com/wongcyrus/a4e726b961260395efa7811cab0b4516)
* Create virtualenv and add to bashrc and source
`python3 -m venv ~/.venv && echo 'source ~/.venv/bin/activate' >> ~/.bashrc && source ~/.bashrc`
* cd into checkout and run `make install`
* Preview running FastAPI app after running:  python main.py

<img width="1835" alt="Screen Shot 2022-09-28 at 12 32 52 PM" src="https://user-images.githubusercontent.com/58792/192836641-cd7ef757-4a4b-4722-bb17-d88980f4e9d4.png">

 * Create ECR repository by right-click in Cloud9
 
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 34 44 PM" src="https://user-images.githubusercontent.com/58792/192837619-b4ebd0fc-d464-4c06-a382-0a25c6028579.png">

* Navigate to ECR repo created <cdfastapi> or whatever you named it and follow "push" instructions
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 36 45 PM" src="https://user-images.githubusercontent.com/58792/192838151-ca89bdc1-bb99-40dc-ace1-f059e07ba5f6.png">

* Navigate to AWS App Runner and Setup Continuous Delivery using ECR
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 41 21 PM" src="https://user-images.githubusercontent.com/58792/192839558-7f1f0e55-7f5b-4af6-99f1-66d0512a41d6.png">

* Setup AWS Code Build to push container after each build (which triggers auto-deploy)  
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 50 19 PM" src="https://user-images.githubusercontent.com/58792/192843483-e0a48ae6-95c1-4758-8928-40c33939cb9f.png">

  
See following [buildspec.yml](https://github.com/nogibjj/fastapi-from-zero/blob/main/buildspec.yml)
and [Makefile](https://github.com/nogibjj/fastapi-from-zero/blob/main/Makefile)


## Things to Cover

* Linting Dockerfile and also dealing with containers

## Tips

* Great way to find a package version: `pip freeze | grep ipython`
