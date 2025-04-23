-- This section converts the SaleDate column to a standard Date format. It initially selects and converts the data, then adds a new column SaleDateConverted to store the cleaned date.

SELECT
    SaleDate,
    CONVERT(Date, SaleDate)
FROM
    NashvilleHousing;

UPDATE
    NashvilleHousing
SET
    SaleDate = CONVERT(Date, SaleDate);

ALTER TABLE
    NashvilleHousing
ADD
    SaleDateConverted Date;

UPDATE
    NashvilleHousing
SET
    SaleDateConverted = CONVERT(Date, SaleDate);

SELECT
    SaleDateConverted,
    SaleDate
FROM
    NashvilleHousing;