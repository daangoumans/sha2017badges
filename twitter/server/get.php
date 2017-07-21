<?php
//We use already made Twitter OAuth library
//https://github.com/mynetx/codebird-php
require_once ('codebird.php');

//Twitter OAuth Settings
$CONSUMER_KEY = '';
$CONSUMER_SECRET = '';
$ACCESS_TOKEN = '';
$ACCESS_TOKEN_SECRET = '';

//Get authenticated
Codebird\Codebird::setConsumerKey($CONSUMER_KEY, $CONSUMER_SECRET);
$cb = Codebird\Codebird::getInstance();
$cb->setToken($ACCESS_TOKEN, $ACCESS_TOKEN_SECRET);

//retrieve parameters
//https://dev.twitter.com/rest/reference/get/search/tweets
if (isset($_GET['hashtag'])) {
        $hashtag = $_GET['hashtag'];
    }else{
        // Fallback behaviour goes here
		$hashtag = 'sha2017';
    }

//retrieve posts
$q = '%23'.$hashtag;
$count = 100;
$api = 'search_tweets';

//https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline
//https://dev.twitter.com/docs/api/1.1/get/search/tweets
$params = array(
'screen_name' => $q,
'q' => $q,
'count' => $count,
);

//Make the REST call

$tempdata = $cb->$api($params);

$data = (array)$tempdata;
//Output result in JSON, getting it ready for jQuery to process
echo json_encode($data);
?>
