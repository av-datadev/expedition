-- This part addresses missing PropertyAddress values. It joins the table to itself based on ParcelID and where UniqueID is different, then uses ISNULL to populate missing addresses where a matching ParcelID has a known address.

SELECT
    *
FROM
    NashvilleHousing
WHERE
    PropertyAddress IS NULL;

SELECT
    a.ParcelID,
    a.PropertyAddress,
    b.ParcelID,
    b.PropertyAddress,
    ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM
    NashvilleHousing a
    JOIN NashvilleHousing b ON a.ParcelID = b.ParcelID
    AND a.[UniqueID ] <> b.[UniqueID ]
WHERE
    a.PropertyAddress IS NULL;

UPDATE
    a
SET
    PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM
    NashvilleHousing a
    JOIN NashvilleHousing b ON a.ParcelID = b.ParcelID
    AND a.[UniqueID ] <> b.[UniqueID ]
WHERE
    a.PropertyAddress IS NULL;

SELECT
    *
FROM
    NashvilleHousing
WHERE
    PropertyAddress IS NULL;