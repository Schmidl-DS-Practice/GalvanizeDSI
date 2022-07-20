--PHQ-9 Demographic Reporting

SELECT DISTINCT 
MYC_MESG.MESSAGE_ID as Q_REQUEST_MESG_ID,
EMP.PROV_NAME as PROV_THAT_SENT_MESG,
EMP.PROV_SPEC as PROV_THAT_SENT_MESG_SPEC,
PATIENT.PAT_MRN_ID as Q_REQUEST_SENT_TO_MRN,
CAST(((((MYC_MESG.CREATED_TIME(DATE))(INT))-((PATIENT.BIRTH_DATE(DATE))(INT))) *.0001) as SMALLINT) as PATIENT_AGE,
CASE 
	When PATIENT_AGE < 13 then '0-12'
	When PATIENT_AGE >=12 and PATIENT_AGE < 18 then '13-17'
	When PATIENT_AGE >=13 and PATIENT_AGE < 30 then '18-29'
	When PATIENT_AGE >=30 and PATIENT_AGE < 40 then '30-39'
	When PATIENT_AGE >=40 and PATIENT_AGE < 50 then '40-49'
	When PATIENT_AGE >=50 and PATIENT_AGE < 60 then '50-59'
	When PATIENT_AGE >=60 and PATIENT_AGE < 70 then '60-69'
	When PATIENT_AGE >=70 and PATIENT_AGE < 80 then '70-79'
	When PATIENT_AGE >=80 and PATIENT_AGE < 90 then '80-89'
	When PATIENT_AGE >=90 and PATIENT_AGE < 100 then '90-99'
	When PATIENT_AGE >= 100 then '100+'
		Else 'Unrecognized Age' END as PAT_AGE_GROUP,
ZC_SEX.NAME as PAT_GENDER,
MYC_MESG.CREATED_TIME as Q_REQUEST_MESG_CREATE_TIME,
MYC_MESG.SUBJECT as Q_REQUEST_MESG_SUBJECT,
CL_QFORM.FORM_NAME as Q_REQUEST_FORM_SENT,
MYC_MES_RESPONSE.MESSAGE_ID as RESPONSE_MESG_ID,
MYC_MES_RESPONSE.CREATED_TIME as RESPONSE_MESG_CREATE_TIME, 
(RESPONSE_MESG_CREATE_TIME-Q_REQUEST_MESG_CREATE_TIME) DAY(4) TO MINUTE as TIME_DIFF_BETWEEN_MESGS, --The Time between when the message was sent and when it was responded to (Format: Day Hour:Minute)
MYC_MES_RESPONSE.SUBJECT as RESPONSE_MESG_SUBJECT,
MYC_MES_RESPONSE.QUEST_ANSWER as TOTAL_SCORE,
CASE When QUESTION9.QUEST_ANSWER = 'Not at all' then 'Negative'
		When QUESTION9.QUEST_ANSWER is Null then Null
		Else 'Positive' END as QUESITON_9_RESP

FROM MYC_MESG
Inner Join MYC_MESG_QUESR on MYC_MESG_QUESR.MESSAGE_ID=MYC_MESG.MESSAGE_ID
Inner Join PAT_MYC_MESG PAT_MESG on PAT_MESG.MYCHART_MESSAGE_ID=MYC_MESG.MESSAGE_ID
Inner Join PATIENT PATIENT on PATIENT.PAT_ID=PAT_MESG.PAT_ID
Left Join (Select Distinct CLARITY_EMP.NAME as PROV_NAME, CLARITY_EMP.PROV_ID, ZC_SPECIALTY.NAME as PROV_SPEC, CLARITY_EMP.USER_ID
				From CLARITY_EMP 
				Left Join CLARITY_SER on CLARITY_EMP.PROV_ID=CLARITY_SER.PROV_ID
				Left Join CLARITY_SER_SPEC on CLARITY_SER.PROV_ID=CLARITY_SER_SPEC.PROV_ID 
				Left Join ZC_SPECIALTY on CLARITY_SER_SPEC.SPECIALTY_C=ZC_SPECIALTY.SPECIALTY_C 
				Where CLARITY_SER_SPEC.LINE='1'
				) as EMP on EMP.USER_ID=MYC_MESG.FROM_USER_ID --Provider Information
Left Outer Join ZC_SEX ZC_SEX on PATIENT.SEX_C=ZC_SEX.RCPT_MEM_SEX_C
Inner Join CL_QFORM on CL_QFORM.FORM_ID=MYC_MESG_QUESR.ALLOW_QUESR_ID --questionnaires linked to this message. 
Left Join (Select Distinct MYC_MESG.MESSAGE_ID, CREATED_TIME, SUBJECT, PARENT_MESSAGE_ID, PAT_MRN_ID, CL_QANSWER_QA.QUEST_ANSWER
			From MYC_MESG MYC_MESG
 			Left Outer Join  MYC_MESG_QUESR_ANS MYC_MESG_QUESR_ANS on MYC_MESG_QUESR_ANS.MESSAGE_ID=MYC_MESG.MESSAGE_ID
 			Left Outer Join CL_QANSWER CL_QANSWER on MYC_MESG_QUESR_ANS.QUESR_ANS_ID=CL_QANSWER.ANSWER_ID
 			Left Outer Join PATIENT PATIENT on MYC_MESG.PAT_ID=PATIENT.PAT_ID
 			Left Outer Join CL_QANSWER_QA CL_QANSWER_QA on CL_QANSWER.ANSWER_ID=CL_QANSWER_QA.ANSWER_ID
			Inner Join CL_QQUEST_OVTM CL_QQUEST_OVTM on (CL_QANSWER_QA.QUEST_DATE_REAL=CL_QQUEST_OVTM.CONTACT_DATE_REAL) and (CL_QANSWER_QA.QUEST_ID=CL_QQUEST_OVTM.QUEST_ID)
				Where SUBJECT = 'Questionnaire Submission'
				And CL_QANSWER_QA.QUEST_ID='12477488') as MYC_MES_RESPONSE on MYC_MESG.MESSAGE_ID=MYC_MES_RESPONSE.PARENT_MESSAGE_ID --Total Score Answer
Left Join (Select Distinct MYC_MESG.MESSAGE_ID, PARENT_MESSAGE_ID, CL_QANSWER_QA.QUEST_ANSWER
			From MYC_MESG MYC_MESG
 			Left Outer Join  MYC_MESG_QUESR_ANS MYC_MESG_QUESR_ANS on MYC_MESG_QUESR_ANS.MESSAGE_ID=MYC_MESG.MESSAGE_ID
 			Left Outer Join CL_QANSWER CL_QANSWER on MYC_MESG_QUESR_ANS.QUESR_ANS_ID=CL_QANSWER.ANSWER_ID
 			Left Outer Join CL_QANSWER_QA CL_QANSWER_QA on CL_QANSWER.ANSWER_ID=CL_QANSWER_QA.ANSWER_ID
			Inner Join CL_QQUEST_OVTM CL_QQUEST_OVTM on (CL_QANSWER_QA.QUEST_DATE_REAL=CL_QQUEST_OVTM.CONTACT_DATE_REAL) and (CL_QANSWER_QA.QUEST_ID=CL_QQUEST_OVTM.QUEST_ID)
				Where SUBJECT = 'Questionnaire Submission'
				And CL_QANSWER_QA.QUEST_ID='12477485') as QUESTION9 on MYC_MESG.MESSAGE_ID=QUESTION9.PARENT_MESSAGE_ID --Question 9 Answer

WHERE
CL_QFORM.FORM_ID='441432' --PHQ-9 Teen Question Form
And PAT_MESG.PAT_ID not in (Select Distinct PAT_ID From PATIENT_TYPE Where PATIENT_TYPE_C='1214') --Test Patient Elimination


