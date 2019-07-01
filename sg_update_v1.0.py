import boto3

### Customizable variables:

temp = open('sg.txt','r').read().splitlines()
for security_group_id in temp:
    profile = "dev"
    print(security_group_id)
#security_group_id = raw_input("Enter security group id : ")
    region = "ap-southeast-1"
####
# Start a session, specifying profile credentials and region:
    session = boto3.session.Session(profile_name=(profile),region_name=(region))
    ec2 = session.resource('ec2')
    SG = ec2.SecurityGroup(security_group_id)
    print(SG)
#Now, we add the new rules using IPs from the CSV:
    SG.authorize_ingress(IpProtocol="tcp",CidrIp="X.X.X.X/32",FromPort=33022,ToPort=33022)
    SG.authorize_ingress(IpProtocol="tcp",CidrIp="X.X.X.X/32",FromPort=33022,ToPort=33022)
# second, we remove all existing rules in the group:
    SG.revoke_ingress(IpProtocol="tcp", CidrIp="X.X.X.X/32", FromPort=22, ToPort=22)
    SG.revoke_ingress(IpProtocol="tcp", CidrIp="X.X.X.X/32", FromPort=22, ToPort=22)
SG.revoke_ingress(IpPermissions=[{'FromPort': 22, 'IpProtocol': 'tcp','Ipv6Ranges': [{'CidrIpv6': '::/0',},],'ToPort': 22,},],)
sg_group.close()


aws ec2 revoke-security-group-ingress --group-id XXXXXXXXX --ip-permissions [{'IpProtocol': '-1','Ipv6Ranges': [{'CidrIpv6': '::/0',},],},]
