"""
문제 설명
신한DS는 신한금융그룹 디지털 통합 교육 플랫폼 ‘SCOOL’ 을 구축하여 그룹사에 디지털 관련 컨텐츠를 제공하고 있습니다.

아래는 SCOOL 플랫폼에서 사용하는 테이블 일부 입니다.



* 사용자정보 테이블 : USER_INFO

user_idx	user_name	group_code	register_date	update_date
1	신한이	S002	2021-07-13 12:42:17	2021-07-13 12:42:17
2	김신한	S004	2021-07-27 14:24:30	2021-08-22 16:04:33
3	한신이	S003	2021-08-11 10:12:47	2021-08-11 10:12:47




* 그룹사 정보 테이블 : GROUP_INFO

group_code	group_name
S001	신한금융지주
S002	신한은행




* 수강시간정보 테이블 : LECTURE_HISTORY

lecture_history_idx	user_idx	lecture_name	study_time	register_date
1	7	빅데이터 서비스 Trend	27	2021-08-12 10:12:17
2	9	AI 현업 적용 기획	48	2021-08-26 12:42:34


SCOOL 플랫폼에서 전체 그룹사 대상으로 우수 수강자 10명을 뽑을려고 합니다.

수강시간 순위 / 그룹사명 / 수강자명 / 수강시간 순으로 조회하는 SQL문을 작성해주세요.

입력
USER_INFO, GROUP_INFO, LECTURE_HISTORY 테이블에 Dummy data가 입력되어 있습니다.

출력
수강시간이 많은 순으로 10명의 순서, 그룹사명, 사용자명, 학습시간 을 출력하세요.

같은 순위일 경우 같은 등수로 표시하고, 중복된 수만큼 건너뛰어 다음 등수를 표시하며 USER_NAME 의 오름차순 으로 정렬합니다.

"""


-- rank 매기기 전에 미리 랭킹기준과 이름순으로 정렬했어야...
-- 또는 rank 매기고 나서 랭킹기준, 이름순으로 정렬하면 되는거잖아..!!! 아악..

SELECT RANK() OVER (ORDER BY total_study_time DESC) rank_no,
group_name, user_name, total_study_time

FROM
(SELECT (
  SELECT GI.group_name FROM GROUP_INFO GI
  WHERE GI.group_code = UI.group_code
	) as group_name,
  user_name, total_study_time

FROM
(SELECT user_idx, sum(study_time) as total_study_time
FROM LECTURE_HISTORY
GROUP BY user_idx
ORDER BY total_study_time DESC) TMP

LEFT JOIN USER_INFO UI

ON UI.user_idx = TMP.user_idx

ORDER BY total_study_time DESC, user_name ASC        <======###################이거!!!!! ㅠㅠㅠㅠㅠ

) AS TMP2

ORDER BY rank_no DESC, user_name ASC        <======############################ 또는 이거!!!!! ㅠㅠㅠㅠㅠ
LIMIT 10
