-- removing dulicates

WITH
    RowNumCTE AS (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY
                    ParcelID,
                    PropertyAddress,
                    SalePrice,
                    SaleDate,
                    LegalReference
                ORDER BY
                    UniqueID
            ) row_num
        FROM
            NashvilleHousing
    )
SELECT
    *
FROM
    RowNumCTE
WHERE
    row_num > 1
ORDER BY
    PropertyAddress;

WITH
    RowNumCTE AS (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY
                    ParcelID,
                    PropertyAddress,
                    SalePrice,
                    SaleDate,
                    LegalReference
                ORDER BY
                    UniqueID
            ) row_num
        FROM
            NashvilleHousing
    )
DELETE
FROM
    RowNumCTE
WHERE
    row_num > 1;

SELECT
    *
FROM
    NashvilleHousing;