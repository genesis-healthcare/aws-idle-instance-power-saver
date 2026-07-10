# resources.py

# 各サービスごとのリソースリスト（EC2, ECS, RDS, Aurora, App Runner）
EC2_INSTANCES = [
    "i-0d0e12c4b5afcddb2",  # arcadia-stg
    "i-0b123e2ababa7eb0b",  # Confy-dev
    "i-04e1d9dc73eb6b49c",  # ec-cube-offline-stg_1
    "i-0bf3b2e4f8cf8ca1c",  # ec-cube-online-stg_1
    "i-0fad20ccbea15cc89",  # FSx-stg
    "i-09e01f85d66879fd8",  # ganesha-stg
    "i-035f2e2ec4312a381",  # GhAsia_FoodValue_Dev
    "i-00670cdce63c4a0c6",  # phoenix-stg
    "i-03ffbcbdc7e32fe92",  # yebisu-stg
   #  "i-01b17e0811a134558",  # kmu-workbench
    "i-098d831dcff55a7c5",  # domo
    "i-077ec2a0f55016705",  # domo_workbench
]

ECS_CLUSTERS = [
    # "AdamChatEditorStg",
    "canopus-dev",
    "canopus-stg",
    "copen-dev",
    "CvBackyardChkDev",
    "CvBackyardChkStg",
    "CvBackyardDev",
    "CvBackyardPMADev",
    "CvBackyardPMAStg",
    "CvBackyardPMAPrd",
    "CvBackyardStg",
    "deep-partner-dev",
    "GaiaSeachLpSiteDev",
    "genelife-app-activityrecord-dev",
    "genelife-app-bff-dev",
    "genelife-app-genebank-dev",
    "genelife-app-listitem-dev",
    "genelife-app-notification-dev",
    "genelife-app-phpmyadmin-dev",
    "genelife-app-pointitem-dev",
    "genelife-app-publication-dev",
    "genelife-app-renaissance-dev",
    "genelife-app-survey-dev",
    "genelife-shinagawa-front-dev",
    "GenesisProStg2",
    "MealApiStg",
    "takanawa-stg",
    "ximen-worker-staging",
    "tokyo-stg",
]

RDS_INSTANCES = [
    "adam-chat",
    "adamrecords",
    "aurora-demo",
    "copen-dev",
    "deep-partner-dev",
    "genelife-app-dev",
    "gh-staging",
    "ghsecurity",
    "phoenix-dev",
    "phoenix-stg",
    "sherpa-stg",
    "takanawa-dev",
    "teru-stg",
    "domo",
]

AURORA_CLUSTERS = [
    "arcadia-stg",
    "cv-backyard-dev",
    "cv-backyard-stg",
    "deep-stg",
    "ganesha-stg",
    "takanawa-stg",
    "yebisu-dev",
    "yebisu-stg",
    "ec-cube-stg",
    "ec-cube-m57-stg2-cluster",
    "ec-cube-offline-prd",
    "ec-cube-online-prd",
    # "kmu-db",
    "ximen-stg",
    "tokyo-back-stg",
    "nalims-stg",
]

APP_RUNNER_SERVICES = [
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/teru-patient_stg/dfec9008f2a647feb181ce852b931d29",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/teru-doctor_stg/5cc2cc57efd64e288de48020d7ae0f8e",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/gaia-front_dev/af7a157691964b8eafe84ed44c498cf0",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/gaia2-back_dev/ddbc5688910d4866850e1033ae7c58d1",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/edomons/83556c8c9db74b79981da3774e6d6718",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/paper-report-dev/167c29be0cea49139458aa5431632f07",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen_stg/44e13be890b54358ac7d9cf700bbeb40",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/myself-stg/6ffc6f6356034d9688c8581038a9f959",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen-back_stg/a56640c318d34b2da1fd21bcbeb96ae3",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen-front_stg/21ea619e2f694daab37225aa12491737",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen-front-stg/817d2a093a2f453394c1cd4774c8f121",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/ghbio-genelink-staging/20d4ca4d36894580a270484b0c369c9d",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/genovision-pgx-stg/3a68ec19900443608f6da9190ed54f58",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/nalims-front-stg/ef3be2e3be93428fb950c77cef71f9ac",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/nalims-back-stg/c0dd8a66ea7649ffaaa7079f58782f7e",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/tokyo-front-stg/0cdfef522b854b5a869bfd2116ce5672",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/tokyo-back-stg/f2c4ba3206b54b7986aff14eaf9512b6",
]

ON_DEMAND_RESOURCES = [
	# EC2
    "i-0b123e2ababa7eb0b",  # Confy-dev
    "i-0fad20ccbea15cc89",  # FSx-stg
    "i-00670cdce63c4a0c6",  # phoenix-stg
    "i-098d831dcff55a7c5",  # domo
    "i-077ec2a0f55016705",  # domo_workbench
    # ECS
    "canopus-dev",
    "canopus-stg",
    "copen-dev",
    "CvBackyardChkDev",
    "CvBackyardChkStg",
    "CvBackyardDev",
    "CvBackyardStg",
    "CvBackyardPMADev",
    "genelife-app-listitem-dev",
    "GaiaSeachLpSiteDev",
    "GenesisProStg2",
    # RDS
    "adam-chat",
    "adamrecords",
    "aurora-demo",
    "copen-dev",
    "gh-staging",
    "ghsecurity",
    "phoenix-dev",
    "phoenix-stg",
    "sherpa-stg",
    "teru-stg",
    "domo",
    # Aurora
    "cv-backyard-dev",
    "cv-backyard-stg",
    "ec-cube-stg",
    "ec-cube-offline-prd",
    "ec-cube-online-prd",
    # "ximen-stg",
    # App Runner
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/teru-patient_stg/dfec9008f2a647feb181ce852b931d29",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/teru-doctor_stg/5cc2cc57efd64e288de48020d7ae0f8e",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/gaia-front_dev/af7a157691964b8eafe84ed44c498cf0",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/gaia2-back_dev/ddbc5688910d4866850e1033ae7c58d1",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/edomons/83556c8c9db74b79981da3774e6d6718",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/paper-report-dev/167c29be0cea49139458aa5431632f07",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen_stg/44e13be890b54358ac7d9cf700bbeb40",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen-front_stg/21ea619e2f694daab37225aa12491737",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/ximen-back_stg/a56640c318d34b2da1fd21bcbeb96ae3",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/myself-stg/6ffc6f6356034d9688c8581038a9f959",
    "arn:aws:apprunner:ap-northeast-1:934400637619:service/genovision-pgx-stg/3a68ec19900443608f6da9190ed54f58",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/tokyo-front-stg/0cdfef522b854b5a869bfd2116ce5672",
    # "arn:aws:apprunner:ap-northeast-1:934400637619:service/tokyo-back-stg/f2c4ba3206b54b7986aff14eaf9512b6",
]

