-- This 1  section splits the PropertyAddress into Address and City using SUBSTRING and CHARINDEX. It then adds new columns to store these separated values. For OwnerAddress, it uses PARSENAME after replacing commas with periods to split it into Address, City, and State.


SELECT
    PropertyAddress
FROM
    NashvilleHousing;

SELECT
    SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1) AS Address,
    SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyAddress)) AS City
FROM
    NashvilleHousing;

ALTER TABLE
    NashvilleHousing
ADD
    PropertySplitAddress Nvarchar(255);

UPDATE
    NashvilleHousing
SET
    PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1);

ALTER TABLE
    NashvilleHousing
ADD
    PropertySplitCity Nvarchar(255);

UPDATE
    NashvilleHousing
SET
    PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyAddress));

SELECT
    *
FROM
    NashvilleHousing;

SELECT
    OwnerAddress
FROM
    NashvilleHousing;

SELECT
    PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
    PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
    PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
FROM
    NashvilleHousing;

ALTER TABLE
    NashvilleHousing
ADD
    OwnerSplitAddress Nvarchar(255);

UPDATE
    NashvilleHousing
SET
    OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3);

ALTER TABLE
    NashvilleHousing
ADD
    OwnerSplitCity Nvarchar(255);

UPDATE
    NashvilleHousing
SET
    OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2);

ALTER TABLE
    NashvilleHousing
ADD
    OwnerSplitState Nvarchar(255);

UPDATE
    NashvilleHousing
SET
    OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1);

SELECT
    *
FROM
    NashvilleHousing;