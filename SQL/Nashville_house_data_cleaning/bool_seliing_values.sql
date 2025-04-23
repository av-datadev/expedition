-- This part standardizes the SoldAsVacant column by converting 'Y' to 'Yes' and 'N' to 'No' using a CASE statement within an UPDATE query.


SELECT
    DISTINCT(SoldAsVacant),
    COUNT(SoldAsVacant)
FROM
    NashvilleHousing
GROUP BY
    SoldAsVacant
ORDER BY
    2;

SELECT
    SoldAsVacant,
    CASE
        WHEN SoldAsVacant = 'Y' THEN 'Yes'
        WHEN SoldAsVacant = 'N' THEN 'No'
        ELSE SoldAsVacant
    END
FROM
    NashvilleHousing;

UPDATE
    NashvilleHousing
SET
    SoldAsVacant = CASE
        WHEN SoldAsVacant = 'Y' THEN 'Yes'
        WHEN SoldAsVacant = 'N' THEN 'No'
        ELSE SoldAsVacant
    END;

SELECT
    DISTINCT(SoldAsVacant),
    COUNT(SoldAsVacant)
FROM
    NashvilleHousing
GROUP BY
    SoldAsVacant
ORDER BY
    2;
