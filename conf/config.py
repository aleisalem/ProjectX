# Google Play Store Crawler Configuration
LANG            	= # can be en_US, fr_FR, ...
ANDROID_ID      	= # '38c6523ac43ef9e1'
GOOGLE_LOGIN    	= # 'someone@gmail.com'
GOOGLE_PASSWORD 	= # 'yourpassword'
AUTH_TOKEN      	= None
SEPARATOR       	= '|'

# Directories
X_DIR 		        = # 'some directory"
DOWNLOADS_DIR		= X_DIR + "files/downloads"

# Logging and debug messages
VERBOSE			    = "ON"
LOGGING			    = "ON"
LOG_FILE		    = X_DIR + "/x.log"

# Android SDK paths and constants
ANDROID_SDK 		= # 'some directory'
ANDROID_ADB 		= ANDROID_SDK + "/platform-tools/adb"

# Misc paths
GENYMOTION_PLAYER 	= # '/opt/genymobile/genymotion/player'

# DB-related information
X_DB			    = X_DIR + "/db/x.db"
HASHES_DB		    = X_DIR + "/db/hashes.db"
DB_RECOVERY		    = X_DIR + "/docs/dbrecovery.sql"
