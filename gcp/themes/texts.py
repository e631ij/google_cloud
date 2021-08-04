# This is a sample Python script.

# ------------------------------------------------------------------------------------------------------------------
# SERVICES
# -----------------------------------------------------------------------------------------------------------------------


MAIN_MENU = ["\n1.  IAM",
             "2.  COMPUTE ENGINE",
             "3.  BUCKETS",
             "4.  KMS",
             "X.  Exit"]


IAM_MENU = ["\n1. IAM USERS",
            "2. IAM KEYS",
            "3. IAM POLICY",
            "4. IAM LOGIN PROFILE",
            "B. BACK TO MAIN MENU\n"
            ]


COMPUTE_MENU = ["\n1. INSTANCE",
            "2. KEYPAIR",
            "3. SECURITY GROUPS",
            "4. NETWORK ACL",
            "5. AUTOMATE INSTANCES",
            "B. BACK TO MAIN MENU\n"
            ]


BUCKET_MENU = ["\n1. BUCKET",
           "2. BUCKET WEBSITE",
           "3. IMAGE CRYPTOGRAPHY",
           "X. BACK TO MAIN MENU\n"
           ]


# ----------------------------------------------------------------------------------------------------


SUB_IAM_MENU = ["\n1. Create users",
                "2. Get users",
                "3. Update users",
                "4. delete users",
                "B. Back to IdentityAccessManager Menu\n"
                ]


SUB_IAM_KEYPAIRS_MENU = ["\n1. Get Keypairs",
                         "2. Create Keypairs",
                         "3. delete Keypairs",
                         "B. Back to IdentityAccessManager Menu\n"
                         ]

SUB_KMS_MENU = ["\n1.  Create Customer Master Key",
                    "2.  List Customer Master Keys",
                    "3.  Generate Data Key",
                    "4.  Decrypt Data Key",
                    "5.  Change Region",
                    "6.  Schedule Keys Deletion",
                    "7.  Enable Customer Master Keys",
                    "8.  Disable Customer Master Keys",
                    "9.  Encrypt File",
                    "10.  Decrypt File",
                    "B.  Back to IdentityAccessManager Menu\n"
                ]



SUB_IAM_POLICY_MENU = ["\n1. Get Policy",
                       "2. Attach policy",
                       "3. Detach policy",
                       "B. Back IdentityAccessManager Menu\n"
                      ]


SUB_IAM_LOGINPROFILE_MENU = ["\n1. Create LoginProfile",
                             "2. Check LoginProfile",
                             "2. Delete LoginProfile",
                             "4. Reset LoginProfile",
                             "B. Back IdentityAccessManager Menu\n"
                      ]


SUB_COMPUTE_MENU = ["\n1. Create Instances",
                "2. Get Instances",
                "3. Start Instances",
                "4. Stop Instances",
                "5. Delete Instances",
                "6. Schedule Instances",
                "B. Back ec2 Menu\n"
                ]

SUB_BUCKET_MENU = ["\n1. Get Buckets",
               "2. Create Buckets",
               "3. Upload Files",
               "4. Downloads Files",
               "5. Delete Bucket",
               "6. Delete Object",
               "7. Update Object",
               "8. List Blobs",
               "9. Delete Blob",
               "10. Bucket Information",
               "B. Back to Bucket Menu\n"
               ]


SUB_BUCKET_CRYPTO_MENU = ["\n1. Get Bucket Encryption",
                      "2.  Encrypt Bucket",
                      "3.  Decrypt Bucket",
                      "4.  Delete Bucket Encryption",
                      "B.  Back to S3 Menu\n"
                      ]



# -----------------------------------------------------------------------------------------------------------------------
# TEXT
# -----------------------------------------------------------------------------------------------------------------------

Session_Text = ["Enter the aws_access_key_id= ",
                "Enter the aws_secret_access_key= ",
                "region_name= "
                ]

main_menu_text = ["\nEnter Menu Choice:  "]

main_menu_exit = ["Enter 99 to exit Menu: "]


iam_text_user = ["Enter UserName: ",
                 "Enter NewUserName: ",
                 "Enter NewPassword: ", ]

iam_text_key = ["Enter KeyName: "]

iam_text_policy = ["Enter Policy Name: ", "Enter Scope (ALL | LOCAL | AWS ): "]

compute_text_instance = ["Enter keyName/Instance Name: ",
                     "Enter GroupName: ",
                     "Enter CIDR: ",
                     "Enter SecurityGroup Description (Not more that 50 Letters): ",
                     "Enter the IpProtocol {tcp/udp}: ",
                     "Enter Path to Local UserData: ",
                     "Enter InstanceType(t2.micro|t2.small|t2.medium|t3.nano|t3.micro|t3.small|t3.medium): ",
                     "Enter AvailabilityZone(us-west-2a|us-west-2b|us-east-2a|us-east-1b): ",
                     "Enter VolumeSize (int): ",
                     "Enter VolumeType (standard | io1 | gp2): "]


compute_text_keys = ["Enter KeyName: ",
                 "Enter KeyDir: ",
                 "Enter SecurityGroupName: ",
                 "Enter SecurityGroup Descriptions(50 Letters): "]


KMS_CustomerMasterKeySpec = ['RSA_2048',
                            'RSA_3072',
                            'RSA_4096',
                            'ECC_NIST_P256',
                            'ECC_NIST_P384',
                            'ECC_NIST_P521',
                            'ECC_SECG_P256K1',
                            'SYMMETRIC_DEFAULT']


KMS_ALGORITHM = ['SYMMETRIC_DEFAULT', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256']


KMS_TEXTS = ["Enter CMK Name: ",
             "Enter Desc: ",
             "Enter CMK ID: ",
             "Enter CMK SPEC (RSA_3072 | RSA_4096 | ECC_NIST_P521 | ECC_SECG_P256K1 ): ",
             "Enter Limit: ",
             "Enter REGION: ",
             "Enter FILENAME: ",
             "Enter Schedule Days (int): "
             ]


KMS_Origin = ['AWS_KMS',
              'EXTERNAL',
              'AWS_CLOUDHSM']


KMS_CRYPTOGRAPHY = ["Enter Encryption FILENAME: "
                    ]


bucket_text_words = ["Enter the BucketName: ",
                 "Enter REGION (US-WEST1): ",
                 "Enter FILENAME (/tmp/hello.txt): ",
                 "Enter Download FILEPATH (/home/Public/hello.txt): ",
                 "Enter OBJECTNAME (hello.txt): ",
                 "Enter OBJECTNAME to be Deleted: "
                     ]

text_error = ["\n!!! Please select from the right option !!!\n"]

menu_agreement = ("""

The responsibilities of a program office are varied. These include:

Clearly communicating the open source strategy within and outside the company
Owning and overseeing the execution of the strategy
Facilitating the effective use of open source in commercial products and services
Ensuring high-quality and frequent releases of code to open source communities
Engaging with developer communities and seeing that the company contributes back to other projects effectively
Fostering an open source culture within an organization
Maintaining open source license compliance reviews and oversight

""")








