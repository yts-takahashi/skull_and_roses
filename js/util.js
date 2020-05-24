/**
 * Get the URL parameters
 *
 * @return  url {url} 対象のURL文字列（任意）
 */
const getUrlParameters = function() {
  const parameters = new Object;
  const pairs = location.search.substring(1).split('&');
  pairs.forEach(pair => {
    const keyValue = pair.split('=');
    parameters[keyValue[0]] = keyValue[1];
  });
  return parameters;
}