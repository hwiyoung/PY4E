import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])

'''
C:\Python\Python366\python.exe D:/11_Reference/07_Github/PY4E/Chapter13_WebServices/twitter2.py

Enter Twitter Account:acitrontea
Retrieving https://api.twitter.com/1.1/friends/list.json?oauth_consumer_key=GrWvRL6UUTSnGVl598V0caBHo&oauth_timestamp=1536886812&oauth_nonce=41834932&oauth_version=1.0&screen_name=acitrontea&count=5&oauth_token=163549465-0tY7WFVNFFwOwNoKQ4kyd60R0q8LKiqwGVI0WaDU&oauth_signature_method=HMAC-SHA1&oauth_signature=DYmdLX9hzSZcXL3WHIVApRwZyvY%3D
{
  "users": [
    {
      "id": 205910433,
      "id_str": "205910433",
      "name": "Blippar",
      "screen_name": "blippar",
      "location": "Global",
      "description": "Leading Augmented Reality and Computer Vision company. The Blippar app - its showcase app - is the world's first augmented reality browser using AR, AI & CV.",
      "url": "https://t.co/6Gk7IUcQ7I",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https://t.co/6Gk7IUcQ7I",
              "expanded_url": "http://www.blippar.com",
              "display_url": "blippar.com",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 27656,
      "friends_count": 387,
      "listed_count": 798,
      "created_at": "Thu Oct 21 21:42:59 +0000 2010",
      "favourites_count": 33072,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": true,
      "verified": true,
      "statuses_count": 13902,
      "lang": "en",
      "status": {
        "created_at": "Thu Sep 13 10:26:03 +0000 2018",
        "id": 1040184827666935808,
        "id_str": "1040184827666935808",
        "text": "Today at Tech Retail Week, @mikelaE will speak with @Design_Bridge on what retailers can learn from FMCG brands' us\u2026 https://t.co/sWshkimXxg",
        "truncated": true,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "mikelaE",
              "name": "Mikela Eskenazi Druckman",
              "id": 120599907,
              "id_str": "120599907",
              "indices": [
                27,
                35
              ]
            },
            {
              "screen_name": "Design_Bridge",
              "name": "Design Bridge",
              "id": 94310316,
              "id_str": "94310316",
              "indices": [
                52,
                66
              ]
            }
          ],
          "urls": [
            {
              "url": "https://t.co/sWshkimXxg",
              "expanded_url": "https://twitter.com/i/web/status/1040184827666935808",
              "display_url": "twitter.com/i/web/status/1\u2026",
              "indices": [
                117,
                140
              ]
            }
          ]
        },
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 2,
        "favorite_count": 2,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "FFFFFF",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_tile": false,
      "profile_image_url": "http://pbs.twimg.com/profile_images/378800000534524646/c503807406ec86bd8702f39988bf406f_normal.jpeg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000534524646/c503807406ec86bd8702f39988bf406f_normal.jpeg",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/205910433/1495441834",
      "profile_link_color": "FF9900",
      "profile_sidebar_border_color": "FFFFFF",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "live_following": false,
      "follow_request_sent": false,
      "notifications": false,
      "muting": false,
      "blocking": false,
      "blocked_by": false,
      "translator_type": "none"
    },
    {
      "id": 444987701,
      "id_str": "444987701",
      "name": "NBA Fantasy",
      "screen_name": "NBAFantasy",
      "location": "",
      "description": "The official NBA source for fantasy news, notes, information, and tips.",
      "url": "https://t.co/ixh5HoVFzQ",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https://t.co/ixh5HoVFzQ",
              "expanded_url": "http://www.NBA.com/Fantasy",
              "display_url": "NBA.com/Fantasy",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 196976,
      "friends_count": 564,
      "listed_count": 2134,
      "created_at": "Fri Dec 23 21:46:21 +0000 2011",
      "favourites_count": 91,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": true,
      "statuses_count": 30645,
      "lang": "en",
      "status": {
        "created_at": "Thu Sep 13 23:00:00 +0000 2018",
        "id": 1040374565786943488,
        "id_str": "1040374565786943488",
        "text": "At #14 on our #Fantasy100 countdown is @Jrue_Holiday11!\n\n@GreggSussman of the @FNTSYSportsNet reflects on Holiday's\u2026 https://t.co/Up8PgTVRwh",
        "truncated": true,
        "entities": {
          "hashtags": [
            {
              "text": "Fantasy100",
              "indices": [
                14,
                25
              ]
            }
          ],
          "symbols": [],
          "user_mentions": [
            {
              "screen_name": "Jrue_Holiday11",
              "name": "That Boy Jrue",
              "id": 309516587,
              "id_str": "309516587",
              "indices": [
                39,
                54
              ]
            },
            {
              "screen_name": "GreggSussman",
              "name": "Gregg Sussman",
              "id": 52329829,
              "id_str": "52329829",
              "indices": [
                57,
                70
              ]
            },
            {
              "screen_name": "FNTSYSportsNet",
              "name": "FNTSY Sports Network",
              "id": 1157948778,
              "id_str": "1157948778",
              "indices": [
                78,
                93
              ]
            }
          ],
          "urls": [
            {
              "url": "https://t.co/Up8PgTVRwh",
              "expanded_url": "https://twitter.com/i/web/status/1040374565786943488",
              "display_url": "twitter.com/i/web/status/1\u2026",
              "indices": [
                117,
                140
              ]
            }
          ]
        },
        "source": "<a href=\"https://studio.twitter.com\" rel=\"nofollow\">Media Studio</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 0,
        "favorite_count": 5,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "131516",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://pbs.twimg.com/profile_images/971154391192559617/MVx8hVjg_normal.jpg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/971154391192559617/MVx8hVjg_normal.jpg",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/444987701/1530749982",
      "profile_link_color": "EB6805",
      "profile_sidebar_border_color": "EEEEEE",
      "profile_sidebar_fill_color": "EFEFEF",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "live_following": false,
      "follow_request_sent": false,
      "notifications": false,
      "muting": false,
      "blocking": false,
      "blocked_by": false,
      "translator_type": "none"
    },
    {
      "id": 971314233051885568,
      "id_str": "971314233051885568",
      "name": "LINE Developers",
      "screen_name": "line_developers",
      "location": "Republic of Korea",
      "description": "\ub77c\uc778 \uac1c\ubc1c\uc790 \ube14\ub85c\uadf8\uc640 \ucc44\uc6a9 \ub4f1 \ub2e4\uc591\ud55c \uc18c\uc2dd\uc744 \ud2b8\uc704\ud130\ub85c \uc804\ub2ec\ud574 \ub4dc\ub9bd\ub2c8\ub2e4.",
      "url": "https://t.co/EztBrQ1Ys6",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https://t.co/EztBrQ1Ys6",
              "expanded_url": "https://engineering.linecorp.com/ko/",
              "display_url": "engineering.linecorp.com/ko/",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 206,
      "friends_count": 3,
      "listed_count": 4,
      "created_at": "Wed Mar 07 09:18:54 +0000 2018",
      "favourites_count": 0,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": true,
      "statuses_count": 42,
      "lang": "en",
      "status": {
        "created_at": "Tue Sep 11 08:13:36 +0000 2018",
        "id": 1039426722574172160,
        "id_str": "1039426722574172160",
        "text": "LINE\uc5d0\uc11c\ub294 2018\ub144\ub3c4 \ud558\ubc18\uae30 \uc2e0\uc785 \ubc0f \uc778\ud134 \uac1c\ubc1c\uc790\ub97c \uacf5\uac1c \ucc44\uc6a9 \uc911\uc785\ub2c8\ub2e4. \n\uc2e0\uaddc \uc785\uc0ac\uc790\uc5d0\uac8c\ub294 \ud558\ubc18\uae30 \ub3d9\uae30\ub4e4\uacfc \ud568\uaed8 \ub5a0\ub098\ub294 \uc77c\ubcf8 \ub77c\uc778 \uc624\ud53c\uc2a4\uc5d0\uc11c\uc758 \uae00\ub85c\ubc8c \uc5f0\uc218 \uae30\ud68c\uae4c\uc9c0! \n\ub04c\ub9b0\ub2e4\uba74? \ubc14\ub85c \uc9c0\uae08 \uc9c0\uc6d0\ud558\uc138\uc694\u2026 https://t.co/Bh6Y5BSmYK",
        "truncated": true,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": [
            {
              "url": "https://t.co/Bh6Y5BSmYK",
              "expanded_url": "https://twitter.com/i/web/status/1039426722574172160",
              "display_url": "twitter.com/i/web/status/1\u2026",
              "indices": [
                117,
                140
              ]
            }
          ]
        },
        "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 9,
        "favorite_count": 4,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "ko"
      },
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "000000",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_tile": false,
      "profile_image_url": "http://pbs.twimg.com/profile_images/1022025974735622145/w-dc8SR5_normal.jpg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/1022025974735622145/w-dc8SR5_normal.jpg",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/971314233051885568/1532504937",
      "profile_link_color": "19CF86",
      "profile_sidebar_border_color": "000000",
      "profile_sidebar_fill_color": "000000",
      "profile_text_color": "000000",
      "profile_use_background_image": false,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "live_following": false,
      "follow_request_sent": false,
      "notifications": false,
      "muting": false,
      "blocking": false,
      "blocked_by": false,
      "translator_type": "none"
    },
    {
      "id": 484757080,
      "id_str": "484757080",
      "name": "Pycoders Weekly",
      "screen_name": "pycoders",
      "location": "Ottawa, Canada",
      "description": "Your weekly dose of all things Python! Python tweets by @mgrouchy and @myusuf3.",
      "url": "http://t.co/36bbge1783",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "http://t.co/36bbge1783",
              "expanded_url": "http://www.pycoders.com",
              "display_url": "pycoders.com",
              "indices": [
                0,
                22
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 46605,
      "friends_count": 2,
      "listed_count": 1240,
      "created_at": "Mon Feb 06 13:13:22 +0000 2012",
      "favourites_count": 430,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": false,
      "statuses_count": 7155,
      "lang": "en",
      "status": {
        "created_at": "Thu Sep 13 18:34:01 +0000 2018",
        "id": 1040307629061545984,
        "id_str": "1040307629061545984",
        "text": "pyjson5 | A JSON5 serializer and parser library for Python 3 written in Cython. \u2013 https://t.co/3ZtX0ym3kd",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": [
            {
              "url": "https://t.co/3ZtX0ym3kd",
              "expanded_url": "http://bit.ly/2Io7PdN",
              "display_url": "bit.ly/2Io7PdN",
              "indices": [
                82,
                105
              ]
            }
          ]
        },
        "source": "<a href=\"https://buffer.com\" rel=\"nofollow\">Buffer</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 1,
        "favorite_count": 9,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "1A1B1F",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://pbs.twimg.com/profile_images/429285908953579520/InZKng9-_normal.jpeg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/429285908953579520/InZKng9-_normal.jpeg",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/484757080/1470242918",
      "profile_link_color": "2FC2EF",
      "profile_sidebar_border_color": "181A1E",
      "profile_sidebar_fill_color": "252429",
      "profile_text_color": "666666",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "live_following": false,
      "follow_request_sent": false,
      "notifications": false,
      "muting": false,
      "blocking": false,
      "blocked_by": false,
      "translator_type": "none"
    },
    {
      "id": 915931760,
      "id_str": "915931760",
      "name": "Right vs Wrong",
      "screen_name": "RightVsWrong_",
      "location": "worldwide",
      "description": "",
      "url": null,
      "entities": {
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 186142,
      "friends_count": 73476,
      "listed_count": 300,
      "created_at": "Wed Oct 31 02:00:31 +0000 2012",
      "favourites_count": 37,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": false,
      "statuses_count": 3789,
      "lang": "en",
      "status": {
        "created_at": "Thu Sep 13 17:58:02 +0000 2018",
        "id": 1040298574708240384,
        "id_str": "1040298574708240384",
        "text": "Dumbbell flys shoulder. https://t.co/4YOgcO1FsK",
        "truncated": false,
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": [],
          "media": [
            {
              "id": 1040298562091855872,
              "id_str": "1040298562091855872",
              "indices": [
                24,
                47
              ],
              "media_url": "http://pbs.twimg.com/media/Dm_iB83VsAAnjc6.jpg",
              "media_url_https": "https://pbs.twimg.com/media/Dm_iB83VsAAnjc6.jpg",
              "url": "https://t.co/4YOgcO1FsK",
              "display_url": "pic.twitter.com/4YOgcO1FsK",
              "expanded_url": "https://twitter.com/RightVsWrong_/status/1040298574708240384/photo/1",
              "type": "photo",
              "sizes": {
                "thumb": {
                  "w": 150,
                  "h": 150,
                  "resize": "crop"
                },
                "large": {
                  "w": 750,
                  "h": 750,
                  "resize": "fit"
                },
                "small": {
                  "w": 680,
                  "h": 680,
                  "resize": "fit"
                },
                "medium": {
                  "w": 750,
                  "h": 750,
                  "resize": "fit"
                }
              }
            }
          ]
        },
        "extended_entities": {
          "media": [
            {
              "id": 1040298562091855872,
              "id_str": "1040298562091855872",
              "indices": [
                24,
                47
              ],
              "media_url": "http://pbs.twimg.com/media/Dm_iB83VsAAnjc6.jpg",
              "media_url_https": "https://pbs.twimg.com/media/Dm_iB83VsAAnjc6.jpg",
              "url": "https://t.co/4YOgcO1FsK",
              "display_url": "pic.twitter.com/4YOgcO1FsK",
              "expanded_url": "https://twitter.com/RightVsWrong_/status/1040298574708240384/photo/1",
              "type": "photo",
              "sizes": {
                "thumb": {
                  "w": 150,
                  "h": 150,
                  "resize": "crop"
                },
                "large": {
                  "w": 750,
                  "h": 750,
                  "resize": "fit"
                },
                "small": {
                  "w": 680,
                  "h": 680,
                  "resize": "fit"
                },
                "medium": {
                  "w": 750,
                  "h": 750,
                  "resize": "fit"
                }
              }
            }
          ]
        },
        "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "retweet_count": 15,
        "favorite_count": 64,
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "lang": "en"
      },
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "C0DEED",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_tile": true,
      "profile_image_url": "http://pbs.twimg.com/profile_images/1018159988722659328/NZFYtFzU_normal.jpg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/1018159988722659328/NZFYtFzU_normal.jpg",
      "profile_link_color": "0084B4",
      "profile_sidebar_border_color": "FFFFFF",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": true,
      "live_following": false,
      "follow_request_sent": false,
      "notifications": false,
      "muting": false,
      "blocking": false,
      "blocked_by": false,
      "translator_type": "none"
    }
  ],
  "next_cursor": 1608972537750029313,
  "next_cursor_str": "1608972537750029313",
  "previous_cursor": 0,
  "previous_cursor_str": "0",
  "total_count": null
}
Remaining 14
blippar
   Today at Tech Retail Week, @mikelaE will speak wit
NBAFantasy
   At #14 on our #Fantasy100 countdown is @Jrue_Holid
line_developers
   LINE에서는 2018년도 하반기 신입 및 인턴 개발자를 공개 채용 중입니다. 
신규 입사
pycoders
   pyjson5 | A JSON5 serializer and parser library fo
RightVsWrong_
   Dumbbell flys shoulder. https://t.co/4YOgcO1FsK

Enter Twitter Account:
'''