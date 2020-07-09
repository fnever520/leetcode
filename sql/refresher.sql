-- publisher_info               consumption_info
-- - video_id                   - video_id
-- - video_duration             - user_id
--                              - user_timespend

-- how many minutes worth of video does an average publisher have?
-- how many publishers have at least one user who watched their videos

SELECT SUM(video_duration)/COUNT(distinct video_id) FROM publisher_info


SELECT COUNT(distinct video_id) FROM publisher_info a
INNER JOIN consumption_info b
ON a.video_id = b.video_id



