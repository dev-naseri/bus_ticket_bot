-- black → 0
--
-- brown → 1
--
-- red → 2
--
-- orange → 3
--
-- yellow → 4
--
-- green → 5
--
-- blue → 6
--
-- violet → 7
--
-- grey → 8
--
-- white → 9

UPDATE color_code
SET result = (CASE color1
                WHEN 'black' THEN 0
                WHEN 'brown' THEN 1
                WHEN 'red' THEN 2
                WHEN 'orange' THEN 3
                WHEN 'yellow' THEN 4
                WHEN 'green' THEN 5
                WHEN 'blue' THEN 6
                WHEN 'violet' THEN 7
                WHEN 'grey' THEN 8
                WHEN 'white' THEN 9
             END) * 10
            + (CASE color2
                WHEN 'black' THEN 0
                WHEN 'brown' THEN 1
                WHEN 'red' THEN 2
                WHEN 'orange' THEN 3
                WHEN 'yellow' THEN 4
                WHEN 'green' THEN 5
                WHEN 'blue' THEN 6
                WHEN 'violet' THEN 7
                WHEN 'grey' THEN 8
                WHEN 'white' THEN 9
              END);
