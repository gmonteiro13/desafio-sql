SELECT st.seller_id, s.name AS seller_name, st.team_id, t.name AS team_name
FROM seller_teams st
JOIN sellers s ON st.seller_id = s.id
JOIN teams t ON st.team_id = t.id
ORDER BY st.seller_id, st.team_id;