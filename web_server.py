scp -i assignment.pem scripts/web_server.py ec2-user@18.189.145.15:~
ssh -i assignment.pem ec2-user@18.189.145.15
python3 web_server.py
