/* Leetcode problem 3475: DNA Pattern Recognition. */

SELECT sample_id, dna_sequence, species,
  CASE
    WHEN dna_sequence REGEXP '^ATG' THEN 1
    ELSE 0
  END AS has_start,
  CASE
    WHEN dna_sequence REGEXP '(TAA|TAG|TGA)$' THEN 1
    ELSE 0
  END AS has_stop,
  CASE
    WHEN dna_sequence REGEXP 'ATAT' THEN 1
    ELSE 0
  END AS has_atat,
  CASE
    WHEN dna_sequence REGEXP 'GGG' THEN 1
    ELSE 0
  END AS has_ggg
  FROM Samples
  ORDER BY sample_id;

