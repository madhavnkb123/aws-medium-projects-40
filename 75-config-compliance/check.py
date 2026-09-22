import os,boto3
r=boto3.client("config").get_compliance_summary_by_config_rule()
print("Compliant:",r.get("ComplianceSummary",{}).get("CompliantResourceCount"))
print("Noncompliant:",r.get("ComplianceSummary",{}).get("NonCompliantResourceCount"))