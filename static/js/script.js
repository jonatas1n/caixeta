function discoverCountry(countryID) {
  if (!countryID) return;

  if (!Object.keys(visitedCountries).includes(countryID))
    return openToast('Oops! Este país não foi visitado pelos Beatles.');

  const country = visitedCountries[countryID];
  openPopup(country);
}