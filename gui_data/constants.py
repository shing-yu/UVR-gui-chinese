import platform

#Platform Details
OPERATING_SYSTEM = platform.system()
SYSTEM_ARCH = platform.platform()
SYSTEM_PROC = platform.processor()
ARM = 'arm'

is_macos = False

CPU = 'cpu'
CUDA_DEVICE = 'cuda'
DIRECTML_DEVICE = "privateuseone"

#MAIN_FONT_NAME = "Century Gothic"
OPT_SEPARATOR_SAVE = '─'*25
BG_COLOR = '#0e0e0f'
FG_COLOR = '#13849f'

#Model Types
VR_ARCH_TYPE = 'VR Arc'
MDX_ARCH_TYPE = 'MDX-Net'
DEMUCS_ARCH_TYPE = 'Demucs'
VR_ARCH_PM = 'VR Architecture'
ENSEMBLE_MODE = 'Ensemble Mode'
ENSEMBLE_STEM_CHECK = 'Ensemble Stem'
SECONDARY_MODEL = 'Secondary Model'
DEMUCS_6_STEM_MODEL = 'htdemucs_6s'
DEFAULT = "Default"
ALIGNMENT_TOOL = 'Alignment Tool Options'

SINGLE_FILE = 'SINGLE_FILE'
MULTIPLE_FILE = 'MULTI_FILE'
MAIN_MULTIPLE_FILE = 'MAIN_MULTI_FILE'
CHOOSE_EXPORT_FIR = 'CHOOSE_EXPORT_FIR'

DUAL = "dual"
FOUR_STEM = "fourstem"
ANY_STEM = "Any Stem"

DEMUCS_V3_ARCH_TYPE = 'Demucs v3'
DEMUCS_V4_ARCH_TYPE = 'Demucs v4'
DEMUCS_NEWER_ARCH_TYPES = [DEMUCS_V3_ARCH_TYPE, DEMUCS_V4_ARCH_TYPE]

DEMUCS_V1 = 'v1'
DEMUCS_V2 = 'v2'
DEMUCS_V3 = 'v3'
DEMUCS_V4 = 'v4'

DEMUCS_V1_TAG = 'v1 | '
DEMUCS_V2_TAG = 'v2 | '
DEMUCS_V3_TAG = 'v3 | '
DEMUCS_V4_TAG = 'v4 | '
DEMUCS_NEWER_TAGS = [DEMUCS_V3_TAG, DEMUCS_V4_TAG]

DEMUCS_VERSION_MAPPER = {
            DEMUCS_V1:DEMUCS_V1_TAG,
            DEMUCS_V2:DEMUCS_V2_TAG,
            DEMUCS_V3:DEMUCS_V3_TAG,
            DEMUCS_V4:DEMUCS_V4_TAG}

#Download Center
DOWNLOAD_FAILED = 'Download Failed'
DOWNLOAD_STOPPED = 'Download Stopped'
DOWNLOAD_COMPLETE = 'Download Complete'
DOWNLOAD_UPDATE_COMPLETE = 'Update Download Complete'
SETTINGS_MENU_EXIT = 'exit'
NO_CONNECTION = 'No Internet Connection'
VIP_SELECTION = 'VIP:'
DEVELOPER_SELECTION = 'VIP:'
NO_NEW_MODELS = 'All Available Models Downloaded'
ENSEMBLE_PARTITION = ': '
NO_MODEL = 'No Model Selected'
CHOOSE_MODEL = 'Choose Model'
SINGLE_DOWNLOAD = 'Downloading Item 1/1...'
DOWNLOADING_ITEM = 'Downloading Item'
FILE_EXISTS = 'File already exists!'
DOWNLOADING_UPDATE = 'Downloading Update...'
DOWNLOAD_MORE = 'Download More Models'
IS_KARAOKEE = "is_karaoke"
IS_BV_MODEL = "is_bv_model"
IS_BV_MODEL_REBAL = "is_bv_model_rebalanced"
INPUT_STEM_NAME = 'Input Stem Name'

#Menu Options

AUTO_SELECT = 'Auto'

#LINKS
DOWNLOAD_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/filelists/download_checks.json"
MDX_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_data_new.json"
VR_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/vr_model_data/model_data_new.json"
MDX23_CONFIG_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/mdx_c_configs/"
BULLETIN_CHECK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/bulletin.txt"

DEMUCS_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/demucs_model_data/model_name_mapper.json"
MDX_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_name_mapper.json"

DONATE_LINK_BMAC = "https://www.buymeacoffee.com/uvr5"
DONATE_LINK_PATREON = "https://www.patreon.com/uvr"

#DOWNLOAD REPOS
NORMAL_REPO = "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/"
UPDATE_REPO = "https://github.com/TRvlvr/model_repo/releases/download/uvr_update_patches/"

UPDATE_MAC_ARM_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg"
UPDATE_MAC_X86_64_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg"
UPDATE_LINUX_REPO = "https://github.com/Anjok07/ultimatevocalremovergui#linux-installation"

ISSUE_LINK = 'https://github.com/Anjok07/ultimatevocalremovergui/issues/new'
VIP_REPO = b'\xf3\xc2W\x19\x1foI)\xc2\xa9\xcc\xb67(Z\xf5',\
           b'gAAAAABjQAIQ-NpNMMxMedpKHHb7ze_nqB05hw0YhbOy3pFzuzDrfqumn8_qvraxEoUpZC5ZXC0gGvfDxFMqyq9VWbYKlA67SUFI_wZB6QoVyGI581vs7kaGfUqlXHIdDS6tQ_U-BfjbEAK9EU_74-R2zXjz8Xzekw=='
NO_CODE = 'incorrect_code'

#Extensions
ONNX = '.onnx'
CKPT = '.ckpt'
CKPT_C = '.ckptc'
YAML = '.yaml'
PTH = '.pth'
TH_EXT = '.th'
JSON = '.json'

#GUI Buttons
START_PROCESSING = 'Start Processing'
WAIT_PROCESSING = 'Please wait...'
STOP_PROCESSING = 'Halting process, please wait...'
LOADING_MODELS = 'Loading models...'

#---Messages and Logs----

MISSING_MODEL = 'missing'
MODEL_PRESENT = 'present'

ALL_STEMS = 'All Stems'
VOCAL_STEM = 'Vocals'
INST_STEM = 'Instrumental'
OTHER_STEM = 'Other'
BASS_STEM = 'Bass'
DRUM_STEM = 'Drums'
GUITAR_STEM = 'Guitar'
PIANO_STEM = 'Piano'
SYNTH_STEM = 'Synthesizer'
STRINGS_STEM = 'Strings'
WOODWINDS_STEM = 'Woodwinds'
BRASS_STEM = 'Brass'
WIND_INST_STEM = 'Wind Inst'
NO_OTHER_STEM = 'No Other'
NO_BASS_STEM = 'No Bass'
NO_DRUM_STEM = 'No Drums'
NO_GUITAR_STEM = 'No Guitar'
NO_PIANO_STEM = 'No Piano'
NO_SYNTH_STEM = 'No Synthesizer'
NO_STRINGS_STEM = 'No Strings'
NO_WOODWINDS_STEM = 'No Woodwinds'
NO_WIND_INST_STEM = 'No Wind Inst'
NO_BRASS_STEM = 'No Brass'
PRIMARY_STEM = '主要音轨'
SECONDARY_STEM = '次要音轨'
LEAD_VOCAL_STEM = 'lead_only'
BV_VOCAL_STEM = 'backing_only'
LEAD_VOCAL_STEM_I = 'with_lead_vocals'
BV_VOCAL_STEM_I = 'with_backing_vocals'
LEAD_VOCAL_STEM_LABEL = 'Lead Vocals'
BV_VOCAL_STEM_LABEL = 'Backing Vocals'

VOCAL_STEM_ONLY = f'仅 {VOCAL_STEM}'
INST_STEM_ONLY = f'仅 {INST_STEM}'
PRIMARY_STEM_ONLY = f'仅 {PRIMARY_STEM}'

IS_SAVE_INST_ONLY = f'save_only_inst'
IS_SAVE_VOC_ONLY = f'save_only_voc'

DEVERB_MAPPER = {'Main Vocals Only':VOCAL_STEM, 
                 'Lead Vocals Only':LEAD_VOCAL_STEM_LABEL, 
                 'Backing Vocals Only':BV_VOCAL_STEM_LABEL, 
                 'All Vocal Types':'ALL'}

BALANCE_VALUES = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#Other Constants
DEMUCS_2_SOURCE = ["instrumental", "vocals"]
DEMUCS_4_SOURCE = ["drums", "bass", "other", "vocals"]

DEMUCS_2_SOURCE_MAPPER = {
                        INST_STEM: 0,
                        VOCAL_STEM: 1}

DEMUCS_4_SOURCE_MAPPER = {
                        BASS_STEM: 0,
                        DRUM_STEM: 1,
                        OTHER_STEM: 2,
                        VOCAL_STEM: 3}

DEMUCS_6_SOURCE_MAPPER = {
                        BASS_STEM:0,
                        DRUM_STEM:1,
                        OTHER_STEM:2,
                        VOCAL_STEM:3,
                        GUITAR_STEM:4,
                        PIANO_STEM:5}

DEMUCS_4_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM]
DEMUCS_6_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM, GUITAR_STEM, PIANO_STEM]

DEMUCS_UVR_MODEL = 'UVR_Model'

CHOOSE_STEM_PAIR = 'Choose Stem Pair'

STEM_SET_MENU = (VOCAL_STEM, 
                 INST_STEM, 
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM, 
                 WIND_INST_STEM)

STEM_SET_MENU_ONLY = list(STEM_SET_MENU) + [OPT_SEPARATOR_SAVE, INPUT_STEM_NAME]

STEM_SET_MENU_2 = (
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM, 
                 WIND_INST_STEM,
                 "Noise",
                 "Reverb")

STEM_PAIR_MAPPER = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            LEAD_VOCAL_STEM: BV_VOCAL_STEM,
            BV_VOCAL_STEM: LEAD_VOCAL_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

STEM_PAIR_MAPPER_FULL = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            OTHER_STEM: NO_OTHER_STEM,
            BASS_STEM: NO_BASS_STEM,
            DRUM_STEM: NO_DRUM_STEM,
            GUITAR_STEM: NO_GUITAR_STEM,
            PIANO_STEM: NO_PIANO_STEM,
            SYNTH_STEM: NO_SYNTH_STEM,
            STRINGS_STEM: NO_STRINGS_STEM,
            WOODWINDS_STEM: NO_WOODWINDS_STEM,
            BRASS_STEM: NO_BRASS_STEM,
            WIND_INST_STEM: NO_WIND_INST_STEM,
            NO_OTHER_STEM: OTHER_STEM,
            NO_BASS_STEM: BASS_STEM,
            NO_DRUM_STEM: DRUM_STEM,
            NO_GUITAR_STEM: GUITAR_STEM,
            NO_PIANO_STEM: PIANO_STEM,
            NO_SYNTH_STEM: SYNTH_STEM,
            NO_STRINGS_STEM: STRINGS_STEM,
            NO_WOODWINDS_STEM: WOODWINDS_STEM,
            NO_BRASS_STEM: BRASS_STEM,
            NO_WIND_INST_STEM: WIND_INST_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

NO_STEM = "No "

NON_ACCOM_STEMS = (
            VOCAL_STEM,
            OTHER_STEM,
            BASS_STEM,
            DRUM_STEM,
            GUITAR_STEM,
            PIANO_STEM,
            SYNTH_STEM,
            STRINGS_STEM,
            WOODWINDS_STEM,
            BRASS_STEM,
            WIND_INST_STEM)

MDX_NET_FREQ_CUT = [VOCAL_STEM, INST_STEM]

DEMUCS_4_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM)
DEMUCS_6_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM, GUITAR_STEM, PIANO_STEM)
DEMUCS_2_STEM_OPTIONS = (VOCAL_STEM, INST_STEM)
DEMUCS_4_STEM_CHECK = (OTHER_STEM, BASS_STEM, DRUM_STEM)

#Menu Dropdowns

VOCAL_PAIR = f'{VOCAL_STEM}/{INST_STEM}'
INST_PAIR = f'{INST_STEM}/{VOCAL_STEM}'
OTHER_PAIR = f'{OTHER_STEM}/{NO_OTHER_STEM}'
DRUM_PAIR = f'{DRUM_STEM}/{NO_DRUM_STEM}'
BASS_PAIR = f'{BASS_STEM}/{NO_BASS_STEM}'
FOUR_STEM_ENSEMBLE = '4 Stem Ensemble'
MULTI_STEM_ENSEMBLE = 'Multi-stem Ensemble'

ENSEMBLE_MAIN_STEM = (CHOOSE_STEM_PAIR, VOCAL_PAIR, OTHER_PAIR, DRUM_PAIR, BASS_PAIR, FOUR_STEM_ENSEMBLE, MULTI_STEM_ENSEMBLE)

MIN_SPEC = 'Min Spec'
MAX_SPEC = 'Max Spec'
AUDIO_AVERAGE = 'Average'

MAX_MIN = f'{MAX_SPEC}/{MIN_SPEC}'
MAX_MAX = f'{MAX_SPEC}/{MAX_SPEC}'
MAX_AVE = f'{MAX_SPEC}/{AUDIO_AVERAGE}'
MIN_MAX = f'{MIN_SPEC}/{MAX_SPEC}'
MIN_MIX = f'{MIN_SPEC}/{MIN_SPEC}'
MIN_AVE = f'{MIN_SPEC}/{AUDIO_AVERAGE}'
AVE_MAX = f'{AUDIO_AVERAGE}/{MAX_SPEC}'
AVE_MIN = f'{AUDIO_AVERAGE}/{MIN_SPEC}'
AVE_AVE = f'{AUDIO_AVERAGE}/{AUDIO_AVERAGE}'

ENSEMBLE_TYPE = (MAX_MIN, MAX_MAX, MAX_AVE, MIN_MAX, MIN_MIX, MIN_AVE, AVE_MAX, AVE_MIN, AVE_AVE)
ENSEMBLE_TYPE_4_STEM = (MAX_SPEC, MIN_SPEC, AUDIO_AVERAGE)

BATCH_MODE = 'Batch Mode'
BETA_VERSION = 'BETA'
DEF_OPT = 'Default'
USER_INPUT = "User Input"
OPT_SEPARATOR = '─'*65

CHUNKS = (AUTO_SELECT, '1', '5', '10', '15', '20', 
          '25', '30', '35', '40', '45', '50', 
          '55', '60', '65', '70', '75', '80', 
          '85', '90', '95', 'Full')

BATCH_SIZE = (DEF_OPT, '2', '3', '4', '5', 
          '6', '7', '8', '9', '10')

VOL_COMPENSATION = (AUTO_SELECT, '1.035', '1.08')

MARGIN_SIZE = ('44100', '22050', '11025')

AUDIO_TOOLS = 'Audio Tools'

MANUAL_ENSEMBLE = 'Manual Ensemble'
TIME_STRETCH = 'Time Stretch'
CHANGE_PITCH = 'Change Pitch'
ALIGN_INPUTS = 'Align Inputs'
MATCH_INPUTS = 'Matchering'
COMBINE_INPUTS = 'Combine Inputs'

if OPERATING_SYSTEM == 'Windows' or OPERATING_SYSTEM == 'Darwin':  
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, TIME_STRETCH, CHANGE_PITCH, ALIGN_INPUTS, MATCH_INPUTS)
else:
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, ALIGN_INPUTS, MATCH_INPUTS)

MANUAL_ENSEMBLE_OPTIONS = (MIN_SPEC, MAX_SPEC, AUDIO_AVERAGE, COMBINE_INPUTS)

PROCESS_METHODS = (VR_ARCH_PM, MDX_ARCH_TYPE, DEMUCS_ARCH_TYPE, ENSEMBLE_MODE, AUDIO_TOOLS)

DEMUCS_SEGMENTS = (DEF_OPT, '1', '5', '10', '15', '20', 
                  '25', '30', '35', '40', '45', '50', 
                  '55', '60', '65', '70', '75', '80', 
                  '85', '90', '95', '100')

DEMUCS_SHIFTS = (0, 1, 2, 3, 4, 5, 
                 6, 7, 8, 9, 10, 11, 
                 12, 13, 14, 15, 16, 17, 
                 18, 19, 20)
SEMI_DEF = ['0']
SEMITONE_SEL = (-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12)

NOUT_SEL = (8, 16, 32, 48, 64)
NOUT_LSTM_SEL = (64, 128)

DEMUCS_OVERLAP = (0.25, 0.50, 0.75, 0.99)
MDX_OVERLAP = (DEF_OPT, 0.25, 0.50, 0.75, 0.99)
MDX23_OVERLAP = range(2, 51)
VR_AGGRESSION = range(0, 51)

TIME_WINDOW_MAPPER = {
            "None": None,
            "1": [0.0625],
            "2": [0.125],
            "3": [0.25],
            "4": [0.5],
            "5": [0.75],
            "6": [1],
            "7": [2],
            "Shifts: Low": [0.0625, 0.5],
            "Shifts: Medium": [0.0625, 0.125, 0.5],
            "Shifts: High": [0.0625, 0.125, 0.25, 0.5]
            #"Shifts: Very High": [0.0625, 0.125, 0.25, 0.5, 0.75, 1],
}

INTRO_MAPPER = {
            "Default": [10],
            "1": [8],
            "2": [6],
            "3": [4],
            "4": [2],
            "Shifts: Low": [1, 10],
            "Shifts: Medium": [1, 10, 8],
            "Shifts: High": [1, 10, 8, 6, 4]
            }

VOLUME_MAPPER = {
            "None": (0, [0]),
            "Low": (-4, range(0, 8)),
            "Medium": (-6, range(0, 12)),
            "High": (-6, [x * 0.5 for x in range(0, 25)]),
            "Very High": (-10, [x * 0.5 for x in range(0, 41)])}
            #"Max": (-10, [x * 0.3 for x in range(0, int(20 / 0.3) + 1)])}

PHASE_MAPPER = {
            "None": [0],
            "Shifts Low": [0, 180],
            "Shifts Medium": [0],
            "Shifts High": [0],
            "Shifts Very High": [0],}

NONE_P = "None"
VLOW_P = "Shifts: Very Low"
LOW_P = "Shifts: Low"
MED_P = "Shifts: Medium"
HIGH_P = "Shifts: High"
VHIGH_P = "Shifts: Very High"
VMAX_P = "Shifts: Maximum"

PHASE_SHIFTS_OPT = {
                     NONE_P:190,
                     VLOW_P:180,
                     LOW_P:90,
                     MED_P:45,
                     HIGH_P:20,
                     VHIGH_P:10,
                     VMAX_P:1,}

VR_WINDOW = ('320', '512','1024')
VR_CROP = ('256', '512', '1024')
POST_PROCESSES_THREASHOLD_VALUES = ('0.1', '0.2', '0.3')

MDX_POP_PRO = ('MDX-NET_Noise_Profile_14_kHz', 'MDX-NET_Noise_Profile_17_kHz', 'MDX-NET_Noise_Profile_Full_Band')
MDX_POP_STEMS = ('Vocals', 'Instrumental', 'Other', 'Drums', 'Bass')
MDX_POP_NFFT = ('4096', '5120', '6144', '7680', '8192', '16384')
MDX_POP_DIMF = ('2048', '3072', '4096')
DENOISE_NONE, DENOISE_S, DENOISE_M = 'None', 'Standard', 'Denoise Model'
MDX_DENOISE_OPTION = [DENOISE_NONE, DENOISE_S, DENOISE_M]
MDX_SEGMENTS = list(range(32, 4000+1, 32))

SAVE_ENSEMBLE = 'Save Ensemble'
CLEAR_ENSEMBLE = 'Clear Selection(s)'
MENU_SEPARATOR = 35*'•'
CHOOSE_ENSEMBLE_OPTION = 'Choose Option'
ALL_TYPES = 'ALL'
INVALID_ENTRY = 'Invalid Input, Please Try Again'
ENSEMBLE_INPUT_RULE = '1. Only letters, numbers, spaces, and dashes allowed.\n2. No dashes or spaces at the start or end of input.'
STEM_INPUT_RULE = '1. Only words with no spaces are allowed.\n2. No spaces, numbers, or special characters.'

ENSEMBLE_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_ENSEMBLE, CLEAR_ENSEMBLE]
ENSEMBLE_CHECK = 'ensemble check'
KARAOKEE_CHECK = 'kara check'

AUTO_PHASE = "Automatic"
POSITIVE_PHASE = "Positive Phase"
NEGATIVE_PHASE = "Negative Phase"
OFF_PHASE = "Native Phase"

ALIGN_PHASE_OPTIONS = [AUTO_PHASE, POSITIVE_PHASE, NEGATIVE_PHASE, OFF_PHASE]

SELECT_SAVED_ENSEMBLE = 'Select Saved Ensemble'
SELECT_SAVED_SETTING = 'Select Saved Setting'
ENSEMBLE_OPTION = "Ensemble Customization Options"
MDX_OPTION = "Advanced MDX-Net Options"
DEMUCS_OPTION = "Advanced Demucs Options"
VR_OPTION = "Advanced VR Options"
HELP_OPTION = "Open Information Guide"
ERROR_OPTION = "Open Error Log"
VERIFY_BEGIN = 'Verifying file '
SAMPLE_BEGIN = 'Creating Sample '
MODEL_MISSING_CHECK = 'Model Missing:'
OPTION_LIST = [VR_OPTION, MDX_OPTION, DEMUCS_OPTION, ENSEMBLE_OPTION, ALIGNMENT_TOOL, HELP_OPTION, ERROR_OPTION]

#Menu Strings
VR_MENU ='VR Menu'
DEMUCS_MENU ='Demucs Menu'
MDX_MENU ='MDX-Net Menu'
ENSEMBLE_MENU ='Ensemble Menu'
HELP_MENU ='Help Menu'
ERROR_MENU ='Error Log'
INPUTS_MENU ='Inputs Menu'
ALIGN_MENU ='Align Menu'

# Audio Player
PLAYING_SONG = ": Playing"
PAUSE_SONG = ": Paused"
STOP_SONG = ": Stopped"

SELECTED_VER = 'Selected'
DETECTED_VER = 'Detected'

SAMPLE_MODE_CHECKBOX = lambda v:f'Sample Mode ({v}s)'
REMOVED_FILES = lambda r, e:f'Audio Input Verification Report:\n\nRemoved Files:\n\n{r}\n\nError Details:\n\n{e}'
ADVANCED_SETTINGS = (ENSEMBLE_OPTION, MDX_OPTION, DEMUCS_OPTION, VR_OPTION, HELP_OPTION, ERROR_OPTION)

WAV = 'WAV'
FLAC = 'FLAC'
MP3 = 'MP3'

MP3_BIT_RATES = ('96k', '128k', '160k', '224k', '256k', '320k')
WAV_TYPE = ('PCM_U8', 'PCM_16', 'PCM_24', 'PCM_32', '32-bit Float', '64-bit Float')
GPU_DEVICE_NUM_OPTS = (DEFAULT, '0', '1', '2', '3', '4', '5', '6', '7', '8')

SELECT_SAVED_SET = 'Choose Option'
SAVE_SETTINGS = 'Save Current Settings'
RESET_TO_DEFAULT = 'Reset to Default'
RESET_FULL_TO_DEFAULT = 'Reset to Default'
RESET_PM_TO_DEFAULT = 'Reset All Application Settings to Default'

SAVE_SET_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_SETTINGS, RESET_TO_DEFAULT]

TIME_PITCH = ('1.0', '2.0', '3.0', '4.0')
TIME_TEXT = '_time_stretched'
PITCH_TEXT = '_pitch_shifted'

#RegEx Input Validation
REG_PITCH = r'^[-+]?(1[0]|[0-9]([.][0-9]*)?)$'
REG_TIME = r'^[+]?(1[0]|[0-9]([.][0-9]*)?)$'
REG_COMPENSATION = r'\b^(1[0]|[0-9]([.][0-9]*)?|Auto|None)$\b'
REG_THES_POSTPORCESS = r'\b^([0]([.][0-9]{0,6})?)$\b'
REG_CHUNKS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b'
REG_CHUNKS_DEMUCS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b'
REG_MARGIN = r'\b^[0-9]*$\b'
REG_SEGMENTS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Default)$\b'
REG_SAVE_INPUT = r'\b^([a-zA-Z0-9 -]{0,25})$\b'
REG_INPUT_STEM_NAME = r'^(Wind Inst|[a-zA-Z]{1,25})$'
REG_SEMITONES = r'^-?(20\.00|[01]?\d(\.\d{1,2})?|20)$'
REG_AGGRESSION = r'^[-+]?[0-9]\d*?$'
REG_WINDOW = r'\b^[0-9]{0,4}$\b'
REG_SHIFTS = r'\b^[0-9]*$\b'
REG_BATCHES = r'\b^([0-9]*?|Default)$\b'
REG_OVERLAP = r'\b^([0]([.][0-9]{0,6})?|Default)$\b'#r"(Default|[0-9]+(\.[0-9]+)?)"#
REG_OVERLAP23 = r'\b^([1][0-9]|[2-9][0-9]*|Default)$\b'#r'\b^([2-9][0-9]*?|Default)$\b'
REG_MDX_SEG = r'\b(?:' + '|'.join([str(num) for num in range(32, 1000001, 32)]) + r')\b'
REG_ALIGN = r'^[-+]?[0-9]\d*?$'
REG_VOL_COMP = r'^\d+\.\d{1,9}$'

# Sub Menu
VR_ARCH_SETTING_LOAD = 'Load for VR Arch'
MDX_SETTING_LOAD = 'Load for MDX-Net'
DEMUCS_SETTING_LOAD = 'Load for Demucs'
ALL_ARCH_SETTING_LOAD = 'Load for Full Application'

# Mappers

DEFAULT_DATA = {
        'chosen_process_method': MDX_ARCH_TYPE,
        'vr_model': CHOOSE_MODEL,
        'aggression_setting': 5,
        'window_size': 512,
        'mdx_segment_size': 256,
        'batch_size': DEF_OPT,
        'crop_size': 256, 
        'is_tta': False,
        'is_output_image': False,
        'is_post_process': False,
        'is_high_end_process': False,
        'post_process_threshold': 0.2,
        'vr_voc_inst_secondary_model': NO_MODEL,
        'vr_other_secondary_model': NO_MODEL,
        'vr_bass_secondary_model': NO_MODEL,
        'vr_drums_secondary_model': NO_MODEL,
        'vr_is_secondary_model_activate': False,        
        'vr_voc_inst_secondary_model_scale': 0.9,
        'vr_other_secondary_model_scale': 0.7,
        'vr_bass_secondary_model_scale': 0.5,
        'vr_drums_secondary_model_scale': 0.5,
        'demucs_model': CHOOSE_MODEL, 
        'segment': DEMUCS_SEGMENTS[0],
        'overlap': DEMUCS_OVERLAP[0],
        'overlap_mdx': MDX_OVERLAP[0],
        'overlap_mdx23': '8',
        'shifts': 2,
        'chunks_demucs': CHUNKS[0],
        'margin_demucs': 44100,
        'is_chunk_demucs': False,
        'is_chunk_mdxnet': False,
        'is_primary_stem_only_Demucs': False,
        'is_secondary_stem_only_Demucs': False,
        'is_split_mode': True,
        'is_demucs_combine_stems': True,#
        'is_mdx23_combine_stems': True,#
        'demucs_voc_inst_secondary_model': NO_MODEL,
        'demucs_other_secondary_model': NO_MODEL,
        'demucs_bass_secondary_model': NO_MODEL,
        'demucs_drums_secondary_model': NO_MODEL,
        'demucs_is_secondary_model_activate': False,        
        'demucs_voc_inst_secondary_model_scale': 0.9,
        'demucs_other_secondary_model_scale': 0.7,
        'demucs_bass_secondary_model_scale': 0.5,
        'demucs_drums_secondary_model_scale': 0.5,
        'demucs_stems': ALL_STEMS,
        'demucs_pre_proc_model': NO_MODEL,
        'is_demucs_pre_proc_model_activate': False,
        'is_demucs_pre_proc_model_inst_mix': False,
        'mdx_net_model': CHOOSE_MODEL,
        'chunks': CHUNKS[0],
        'margin': 44100,
        'compensate': AUTO_SELECT,
        'is_denoise': False,#
        'denoise_option': 'None',#
        'phase_option': AUTO_PHASE,
        'phase_shifts': NONE_P,#
        'is_save_align': False,#, 
        'is_match_frequency_pitch': True,#
        'is_match_silence': True,#
        'is_spec_match': False,#
        'is_mdx_c_seg_def': False,
        'is_invert_spec': False, #
        'is_deverb_vocals': False, #
        'deverb_vocal_opt': 'Main Vocals Only', #
        'voc_split_save_opt': 'Lead Only', #
        'is_mixer_mode': False, 
        'mdx_batch_size': DEF_OPT,
        'mdx_voc_inst_secondary_model': NO_MODEL,
        'mdx_other_secondary_model': NO_MODEL,
        'mdx_bass_secondary_model': NO_MODEL,
        'mdx_drums_secondary_model': NO_MODEL,
        'mdx_is_secondary_model_activate': False,        
        'mdx_voc_inst_secondary_model_scale': 0.9,
        'mdx_other_secondary_model_scale': 0.7,
        'mdx_bass_secondary_model_scale': 0.5,
        'mdx_drums_secondary_model_scale': 0.5,
        'mdx_stems': ALL_STEMS,
        'is_save_all_outputs_ensemble': True,
        'is_append_ensemble_name': False,
        'chosen_audio_tool': AUDIO_TOOL_OPTIONS[0],
        'choose_algorithm': MANUAL_ENSEMBLE_OPTIONS[0],
        'time_stretch_rate': 2.0,
        'pitch_rate': 2.0,
        'is_time_correction': True,
        'is_gpu_conversion': False,
        'is_primary_stem_only': False,
        'is_secondary_stem_only': False,
        'is_testing_audio': False,#
        'is_auto_update_model_params': True,#
        'is_add_model_name': False,
        'is_accept_any_input': False,
        'is_task_complete': False,
        'is_normalization': False,
        'is_use_opencl': False,
        'is_wav_ensemble': False,
        'is_create_model_folder': False,
        'mp3_bit_set': '320k',#
        'semitone_shift': '0',#
        'save_format': WAV,
        'wav_type_set': 'PCM_16',
        'device_set': DEFAULT,
        'user_code': '',
        'export_path': '',
        'input_paths': [],
        'lastDir': None,
        'time_window': "3",
        'intro_analysis': DEFAULT,
        'db_analysis': "Medium",
        'fileOneEntry': '',
        'fileOneEntry_Full': '',
        'fileTwoEntry': '',
        'fileTwoEntry_Full': '',
        'DualBatch_inputPaths': [],
        'model_hash_table': {},
        'help_hints_var': True,
        'set_vocal_splitter': NO_MODEL,
        'is_set_vocal_splitter': False,#
        'is_save_inst_set_vocal_splitter': False,#
        'model_sample_mode': False,
        'model_sample_mode_duration': 30
}

SETTING_CHECK = ('vr_model',
               'aggression_setting',
               'window_size',
               'mdx_segment_size',
               'batch_size',
               'crop_size',
               'is_tta',
               'is_output_image',
               'is_post_process',
               'is_high_end_process',
               'post_process_threshold',
               'vr_voc_inst_secondary_model',
               'vr_other_secondary_model',
               'vr_bass_secondary_model',
               'vr_drums_secondary_model',
               'vr_is_secondary_model_activate',
               'vr_voc_inst_secondary_model_scale',
               'vr_other_secondary_model_scale',
               'vr_bass_secondary_model_scale',
               'vr_drums_secondary_model_scale',
               'demucs_model',
               'segment',
               'overlap',
               'overlap_mdx',
               'shifts',
               'chunks_demucs',
               'margin_demucs',
               'is_chunk_demucs',
               'is_primary_stem_only_Demucs',
               'is_secondary_stem_only_Demucs',
               'is_split_mode',
               'is_demucs_combine_stems',#
               'is_mdx23_combine_stems',#
               'demucs_voc_inst_secondary_model',
               'demucs_other_secondary_model',
               'demucs_bass_secondary_model',
               'demucs_drums_secondary_model',
               'demucs_is_secondary_model_activate',
               'demucs_voc_inst_secondary_model_scale',
               'demucs_other_secondary_model_scale',
               'demucs_bass_secondary_model_scale',
               'demucs_drums_secondary_model_scale',
               'demucs_stems',
               'mdx_net_model',
               'chunks',
               'margin',
               'compensate',
               'is_denoise',#
               'denoise_option',#
               'phase_option',#
               'phase_shifts',#
               'is_save_align',#,
               'is_match_silence',
               'is_spec_match',#,
               'is_match_frequency_pitch',#
               'is_mdx_c_seg_def',
               'is_invert_spec',#
               'is_deverb_vocals',#
               'deverb_vocal_opt',#
               'voc_split_save_opt',#
               'mdx_batch_size',
               'mdx_voc_inst_secondary_model',
               'mdx_other_secondary_model',
               'mdx_bass_secondary_model',
               'mdx_drums_secondary_model',
               'mdx_is_secondary_model_activate',
               'mdx_voc_inst_secondary_model_scale',
               'mdx_other_secondary_model_scale',
               'mdx_bass_secondary_model_scale',
               'mdx_drums_secondary_model_scale',
               'is_save_all_outputs_ensemble',
               'is_append_ensemble_name',
               'chosen_audio_tool',
               'choose_algorithm',
               'time_stretch_rate',
               'pitch_rate',
               'is_time_correction',
               'is_primary_stem_only',
               'is_secondary_stem_only',
               'is_testing_audio',#
               'is_auto_update_model_params',#
               'is_add_model_name',
               "is_accept_any_input",
               'is_task_complete',
               'is_create_model_folder',
               'mp3_bit_set',#
               'semitone_shift',#
               'save_format',
               'wav_type_set',
               'device_set',
               'user_code',
               'is_gpu_conversion',
               'is_normalization',
               'is_use_opencl',
               'is_wav_ensemble',
               'help_hints_var',
               'set_vocal_splitter',
               'is_set_vocal_splitter',#
               'is_save_inst_set_vocal_splitter',#
               'model_sample_mode',
               'model_sample_mode_duration',
               'time_window',
               'intro_analysis',
               'db_analysis',
               'fileOneEntry',
               'fileOneEntry_Full',
               'fileTwoEntry',
               'fileTwoEntry_Full',
               'DualBatch_inputPaths'
               )

NEW_LINES = "\n\n"
NEW_LINE = "\n"
NO_LINE = ''

FFMPEG_EXT = (".aac", ".aiff", ".alac" ,".flac", ".FLAC", ".mov", ".mp4", ".MP4", 
              ".m4a", ".M4A", ".mp2", ".mp3", "MP3", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".OGG", ".tta", ".wav", ".wave", ".WAV", ".WAVE", ".wma", ".webm", ".eac3", ".mkv", ".opus", ".OPUS")

FFMPEG_MORE_EXT = (".aa", ".aac", ".ac3", ".aiff", ".alac", ".avi", ".f4v",".flac", ".flic", ".flv",
              ".m4v",".mlv", ".mov", ".mp4", ".m4a", ".mp2", ".mp3", ".mp4", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".tta", ".tty", ".vcd", ".wav", ".wma")
ANY_EXT = ""

# Secondary Menu Constants

VOCAL_PAIR_PLACEMENT = 1, 2, 3, 4
OTHER_PAIR_PLACEMENT = 5, 6, 7, 8
BASS_PAIR_PLACEMENT = 9, 10, 11, 12
DRUMS_PAIR_PLACEMENT = 13, 14, 15, 16

# Drag n Drop String Checks

DOUBLE_BRACKET = "} {"
RIGHT_BRACKET = "}"
LEFT_BRACKET = "{"
#DND CONSTS

MAC_DND_CHECK = ('/Users/',
                 '/Applications/',
                 '/Library/',
                 '/System/')
LINUX_DND_CHECK = ('/home/',
                   '/usr/')
WINDOWS_DND_CHECK = ('A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:')

WOOD_INST_MODEL_HASH = '0ec76fd9e65f81d8b4fbd13af4826ed8'
WOOD_INST_PARAMS = {
    "vr_model_param": "4band_v3",
    "primary_stem": NO_WIND_INST_STEM
                     }

READ_ONLY = 'readonly'

FILE_1 = 'file1'
FILE_2 = 'file2'

FILE_1_LB = 'file1_lb'
FILE_2_LB = 'file1_2b'
BATCH_MODE_DUAL = " : Batch Mode"

CODEC_DICT = {
    'PCM_U8':   {"sample_width": 1, "codec": None},        # 8-bit unsigned PCM
    'PCM_16':   {"sample_width": 2, "codec": None},        # 16-bit signed PCM
    'PCM_24':   {"sample_width": 3, "codec": None},        # 24-bit signed PCM
    'PCM_32':   {"sample_width": 4, "codec": None},        # 32-bit signed PCM
    'FLOAT32':  {"sample_width": None, "codec": "pcm_f32le"},  # 32-bit float
    'FLOAT64':  {"sample_width": None, "codec": "pcm_f64le"}   # 64-bit float
}


# Manual Downloads
VR_PLACEMENT_TEXT = 'Place models in \"models/VR_Models\" directory.'
MDX_PLACEMENT_TEXT = 'Place models in \"models/MDX_Net_Models\" directory.'
DEMUCS_PLACEMENT_TEXT = 'Place models in \"models/Demucs_Models\" directory.'
DEMUCS_V3_V4_PLACEMENT_TEXT = 'Place items in \"models/Demucs_Models/v3_v4_repo\" directory.'
MDX_23_NAME = "MDX23C Model"

# Liscense info
if OPERATING_SYSTEM=="Darwin":
   is_macos = True
   LICENSE_OS_SPECIFIC_TEXT = '• This application is intended for those running macOS Catalina and above.\n' +\
                              '• Application functionality for systems running macOS Mojave or lower is not guaranteed.\n' +\
                              '• Application functionality for older or budget Mac systems is not guaranteed.\n\n'
elif OPERATING_SYSTEM=="Linux":
   LICENSE_OS_SPECIFIC_TEXT = '• This application is intended for those running Linux Ubuntu 18.04+.\n' +\
                              '• Application functionality for systems running other Linux platforms is not guaranteed.\n' +\
                              '• Application functionality for older or budget systems is not guaranteed.\n\n'
elif OPERATING_SYSTEM=="Windows":
   LICENSE_OS_SPECIFIC_TEXT = '• This application is intended for those running Windows 10 or higher.\n' +\
                              '• Application functionality for systems running Windows 7 or lower is not guaranteed.\n' +\
                              '• Application functionality for Intel Pentium & Celeron CPUs systems is not guaranteed.\n\n'

LICENSE_TEXT = lambda a, p:f'Current Application Version: Ultimate Vocal Remover {a}\n' +\
               f'Current Patch Version: {p}\n\n' +\
               'Copyright (c) 2022 Ultimate Vocal Remover\n\n' +\
               'UVR is free and open-source, but MIT licensed. Please credit us if you use our\n' +\
               f'models or code for projects unrelated to UVR.\n\n{LICENSE_OS_SPECIFIC_TEXT}' +\
               'This bundle contains the UVR interface, Python, PyTorch, and other\n' +\
               'dependencies needed to run the application effectively.\n\n' +\
               'Website Links: This application, System or Service(s) may contain links to\n' +\
               'other websites and downloads, and they are solely provided to you as an\n' +\
               'additional convenience. You understand and acknowledge that by clicking\n' +\
               'or activating such links you are accessing a site or service outside of\n' +\
               'this application, and that we do not screen, review, approve, or otherwise\n' +\
               'endorse any content or information contained in these linked websites.\n' +\
               'You acknowledge and agree that we, our affiliates and partners are not\n' +\
               'responsible for the contents of any of these linked websites, including\n' +\
               'the accuracy or availability of information provided by the linked websites,\n' +\
               'and we make no representations or warranties regarding your use of\n' +\
               'the linked websites.\n\n' +\
               'This application is MIT Licensed\n\n' +\
               'Permission is hereby granted, free of charge, to any person obtaining a copy\n' +\
               'of this software and associated documentation files (the "Software"), to deal\n' +\
               'in the Software without restriction, including without limitation the rights\n' +\
               'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n' +\
               'copies of the Software, and to permit persons to whom the Software is\n' +\
               'furnished to do so, subject to the following conditions:\n\n' +\
               'The above copyright notice and this permission notice shall be included in all\n' +\
               'copies or substantial portions of the Software.\n\n' +\
               'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n' +\
               'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n' +\
               'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n' +\
               'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n' +\
               'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n' +\
               'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n' +\
               'SOFTWARE.'

# Message Box Text
INVALID_INPUT = 'Invalid Input', 'The input is invalid.\n\nPlease verify the input still exists or is valid and try again.'
INVALID_EXPORT = 'Invalid Export Directory', 'You have selected an invalid export directory.\n\nPlease make sure the selected directory still exists.'
INVALID_ENSEMBLE = 'Not Enough Models', 'You must select 2 or more models to run ensemble.'
INVALID_MODEL = 'No Model Chosen', 'You must select an model to continue.'
MISSING_MODEL = 'Model Missing', 'The selected model is missing or not valid.'
ERROR_OCCURED = 'Error Occured', '\n\nWould you like to open the error log for more details?\n'
PROCESS_COMPLETE = '\nProcess complete\n'
PROCESS_COMPLETE_2 = 'Process complete\n'

# GUI Text Constants
BACK_TO_MAIN_MENU = 'Back to Main Menu'

# Help Hint Text
INTERNAL_MODEL_ATT = 'This is an internal model setting. \n\n***Avoid changing it unless you\'re certain about it!***'
STOP_HELP = 'Stops ongoing tasks.\n• A confirmation pop-up will appear before stopping.'
SETTINGS_HELP = 'Accesses the main settings and the "Download Center."'
COMMAND_TEXT_HELP = 'Shows the status and progress of ongoing tasks.'
SAVE_CURRENT_SETTINGS_HELP = 'Load or save the app\'s settings.'
PITCH_SHIFT_HELP = ('Choose the pitch for processing tracks:\n\n'
                '• Whole numbers indicate semitones.\n'
                '• Using higher pitches may cut the upper bandwidth, even in high-quality models.\n'
                '• Upping the pitch can be better for tracks with deeper vocals.\n'
                '• Dropping the pitch may take more processing time but works well for tracks with high-pitched vocals.')
AGGRESSION_SETTING_HELP = ('Adjust the intensity of primary stem extraction:\n\n'
                           '• It ranges from -100 - 100.\n'
                           '• Bigger values mean deeper extractions.\n' 
                           '• Typically, it\'s set to 5 for vocals & instrumentals. \n' 
                           '• Values beyond 5 might muddy the sound for non-vocal models.')
WINDOW_SIZE_HELP = ('Select window size to balance quality and speed:\n\n'
                    '• 1024 - Quick but lesser quality.\n'
                    '• 512 - Medium speed and quality.\n'
                    '• 320 - Takes longer but may offer better quality.')
MDX_SEGMENT_SIZE_HELP = ('Pick a segment size to balance speed, resource use, and quality:\n'
                         '• Smaller sizes consume less resources.\n'
                         '• Bigger sizes consume more resources, but may provide better results.\n'
                         '• Default size is 256. Quality can change based on your pick.')
DEMUCS_STEMS_HELP = ('Select a stem for extraction with the chosen model:\n\n'
                     '• All Stems - Extracts all available stems.\n'
                     '• Vocals - Only the "vocals" stem.\n'
                     '• Other - Only the "other" stem.\n'
                     '• Bass - Only the "bass" stem.\n'
                     '• Drums - Only the "drums" stem.')
SEGMENT_HELP = ('Adjust segments to manage RAM or V-RAM usage:\n\n'
               '• Smaller sizes consume less resources.\n'
               '• Bigger sizes consume more resources, but may provide better results.\n'
               '• "Default" picks the optimal size.')

ENSEMBLE_MAIN_STEM_HELP = (
    'Select the stem type for ensembling:\n\n'
    
    f'• {VOCAL_PAIR}:\n'
    '  - Primary Stem: Vocals\n'
    '  - Secondary Stem: Instrumental (mixture minus vocals)\n\n'
    
    f'• {OTHER_PAIR}:\n'
    '  - Primary Stem: Other\n'
    '  - Secondary Stem: No Other (mixture minus "other")\n\n'
    
    f'• {BASS_PAIR}:\n'
    '  - Primary Stem: Bass\n'
    '  - Secondary Stem: No Bass (mixture minus bass)\n\n'
    
    f'• {DRUM_PAIR}:\n'
    '  - Primary Stem: Drums\n'
    '  - Secondary Stem: No Drums (mixture minus drums)\n\n'
    
    f'• {FOUR_STEM_ENSEMBLE}:\n'
    '  - Gathers all 4-stem Demucs models and ensembles all outputs.\n\n'
    
    f'• {MULTI_STEM_ENSEMBLE}:\n'
    '  - The "Jungle Ensemble" gathers all models and ensembles any related outputs.'
)

ENSEMBLE_TYPE_HELP = (
    'Choose the ensemble algorithm for generating the final output:\n\n'
    
    f'• {MAX_MIN}:\n'
    '  - Primary stem processed with "Max Spec" algorithm.\n'
    '  - Secondary stem processed with "Min Spec" algorithm.\n\n'
    
    'Note: For the "4 Stem Ensemble" option, only one algorithm will be displayed.\n\n'
    
    'Algorithm Details:\n'
    
    f'• {MAX_SPEC}:\n'
    '  - Produces the highest possible output.\n'
    '  - Ideal for vocal stems for a fuller sound, but might introduce unwanted artifacts.\n'
    '  - Works well with instrumental stems, but avoid using VR Arch models in the ensemble.\n\n'
    
    f'• {MIN_SPEC}:\n'
    '  - Produces the lowest possible output.\n'
    '  - Ideal for instrumental stems for a cleaner result. Might result in a "muddy" sound.\n\n'
    
    f'• {AUDIO_AVERAGE}:\n'
    '  - Averages all results together for the final output.'
)

ENSEMBLE_LISTBOX_HELP = (
    'Displays all available models for the chosen main stem pair.'
)

if OPERATING_SYSTEM == 'darwin':
   IS_GPU_CONVERSION_HELP = (
      '• 使用GPU进行处理（如果可用）：\n'
      '  - 如果选中，应用程序将尝试使用您的GPU进行更快的处理。\n'
      '  - 如果未检测到GPU，将默认使用CPU进行处理。\n'
      '  - 仅支持MacOS上的VR Arch模型进行GPU处理。\n\n'
      '• 请注意：\n'
      '  - CPU处理速度明显较慢于GPU处理。\n'
      '  - 只有搭载M1芯片的Mac可以用于GPU处理。'
   )
else:
   IS_GPU_CONVERSION_HELP = (
      '• 使用GPU进行处理（如果可用）：\n'
      '  - 如果选中，应用程序将尝试使用您的GPU进行更快的处理。\n'
      '  - 如果未检测到GPU，将默认使用CPU进行处理。\n\n'
      '• 请注意：\n'
      '  - CPU处理速度明显较慢于GPU处理。\n'
      '  - 只有Nvidia GPU可以用于GPU处理。'
   )


IS_TIME_CORRECTION_HELP = ('当选中时，输出将保留输入的原始BPM。')
SAVE_STEM_ONLY_HELP = '允许用户仅保存所选的音轨。'
IS_NORMALIZATION_HELP = '将输出归一化，以防止削波。'
IS_CUDA_SELECT_HELP = '如果您有多个GPU，可以选择使用哪一个进行处理。'
CROP_SIZE_HELP = '**仅与部分模型兼容！**\n\n设置应与训练裁剪大小的值相匹配。如果不确定，请保持不变。'
IS_TTA_HELP = ('此选项执行测试时间增强以提高分离质量。\n\n'
               '注意：选择此选项会增加转换所需的时间。')
IS_POST_PROCESS_HELP = ('此选项可能会识别音频输出中剩余的器乐残留。 \n此选项可能改善某些歌曲的分离。\n\n' +\
                       '注意：选择此选项可能会对转换过程产生不利影响，具体取决于音轨。因此，仅建议作为最后的手段。')
IS_HIGH_END_PROCESS_HELP = '应用程序将镜像输出的缺失频率范围。'
SHIFTS_HELP = ('执行带有输入随机移位的多个预测，并对它们进行平均。\n\n'
              '• 移位次数越多，预测时间越长。 \n- 不建议除非您有GPU。')
OVERLAP_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
               '       - 较高的值可以提供更好的结果，但会导致更长的处理时间。\n'
               '       - 您可以在0.001-0.999之间进行选择')
MDX_OVERLAP_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
               '       - 较高的值可以提供更好的结果，但会导致更长的处理时间。\n'
               '       - 对于非MDX23C模型：您可以在0.001-0.999之间进行选择')
OVERLAP_23_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
                  '       - 较高的值可以提供更好的结果，但会导致更长的处理时间。')
IS_SEGMENT_DEFAULT_HELP = '• 根据所选模型的关联配置文件（yaml）中提供的值设置段大小。'
IS_SPLIT_MODE_HELP = '• 启用\"分段\"。\n• 不推荐取消选择此选项，除非您有强大的个人电脑。'
IS_DEMUCS_COMBINE_STEMS_HELP = '应用程序将通过组合剩余音轨而不是倒置主音轨与混音来创建次要音轨。'
COMPENSATE_HELP = '补偿主音轨的音频，以实现更好的次要音轨。'
IS_DENOISE_HELP = ('• 标准：此设置减少MDX-Net模型产生的噪音。\n' 
                   '       - 此选项仅减少非MDX23模型中的噪音。\n' 
                   '• 降噪模型：此设置使用特殊的降噪模型消除任何MDX-Net模型产生的噪音。\n'
                   '       - 此选项适用于所有MDX-Net模型。\n'
                   '       - 您必须安装“UVR-DeNoise-Lite” VR Arch模型才能使用此选项。\n'
                   '• 请注意：这两个选项都将增加分离时间。')


VOC_SPLIT_MODEL_SELECT_HELP = '• 从主音和伴奏模型列表中选择一个模型，以便通过自动处理音频分离主音和伴奏部分。'
IS_VOC_SPLIT_INST_SAVE_SELECT_HELP = '• 当激活时，您将获得额外的乐器输出，包括：仅包含主音的一个输出和仅包含伴奏的另一个输出。'
IS_VOC_SPLIT_MODEL_SELECT_HELP = ('• 当激活时，此选项将使用卡拉OK模型去除主音或使用背景音乐模型去除伴奏，自动处理生成的声音轨。\n'
                                 '       - 此选项将声音轨分为两个部分：主音和伴奏，提供两个额外的声音输出。\n'
                                 '       - 无论您使用卡拉OK模型还是背景音乐模型，结果都将以相同的方式组织。\n'
                                 '       - 此选项目前在合奏模式下无效。')
IS_DEVERB_OPT_HELP = ('• 选择您希望自动去除混响的声音类型。\n'
                     '       - 例如：选择"仅主音"将仅从主音声音轨中去除混响。')
IS_DEVERB_VOC_HELP = ('• 此选项从声音轨中去除混响。\n'
                     '       - 您必须安装"UVR-DeEcho-DeReverb" VR Arch模型才能使用此选项。\n'
                     '       - 此选项目前在合奏模式下无效。')
IS_FREQUENCY_MATCH_HELP = '将主要声音轨的频率截止匹配到次要声音轨的频率截止。'
CLEAR_CACHE_HELP = '清除用户选择的无法识别的模型的设置。'
IS_SAVE_ALL_OUTPUTS_ENSEMBLE_HELP = '如果启用，将保留所有单独的合奏生成输出。'
IS_APPEND_ENSEMBLE_NAME_HELP = '当启用时，将合奏名称添加到最终输出。'
IS_WAV_ENSEMBLE_HELP = (
    '激活此选项，使用波形而不是频谱图处理合奏算法：\n'
    '• 可能导致增加失真。\n'
    '• 波形合奏比频谱图合奏更快。'
)
DONATE_HELP = '打开官方UVR "Buy Me a Coffee" 外部链接，用于项目捐赠！'
IS_INVERT_SPEC_HELP = (
    '潜在增强次要声音轨质量的选项：\n'
    '• 使用频谱图反转主要声音轨，而不是波形。\n'
    '• 反转方法稍微较慢。'
)
IS_TESTING_AUDIO_HELP = '在保存文件时追加一个10位数字，以避免意外覆盖。'
IS_MODEL_TESTING_AUDIO_HELP = '在输出中追加模型名称，以便在不同模型之间进行比较。'
IS_ACCEPT_ANY_INPUT_HELP = (
    '启用此选项时，允许所有类型的输入，甚至是非音频格式。\n'
    '仅供实验使用，不建议常规使用。'
)
IS_TASK_COMPLETE_HELP = '在处理完成或失败时激活时，播放提示音。'
DELETE_YOUR_SETTINGS_HELP = (
    '包含您保存的设置。在删除所选设置之前，将会要求确认。'
)

SET_STEM_NAME_HELP = '为给定模型选择主音轨。'
IS_CREATE_MODEL_FOLDER_HELP = ('每次转换后，将在导出目录中为输出生成两个新目录。\n\n'
                              '• 示例: \n'
                              '─ 导出目录\n'
                              '   └── 第一个目录（以模型命名）\n'
                              '           └── 第二个目录（以音轨命名）\n'
                              '                    └── 输出文件(们)')
MDX_DIM_T_SET_HELP = INTERNAL_MODEL_ATT
MDX_DIM_F_SET_HELP = INTERNAL_MODEL_ATT

MDX_N_FFT_SCALE_SET_HELP = '指定在模型训练中使用的 N_FFT 大小。'
POPUP_COMPENSATE_HELP = (
    f'为所选模型选择适当的音量补偿。\n'
    f'提醒: {COMPENSATE_HELP}'
)
VR_MODEL_PARAM_HELP = '选择运行所选模型所需的参数。'
CHOSEN_ENSEMBLE_HELP = (
    '默认合奏选择：\n'
    '• 保存当前合奏配置。\n'
    '• 清除所有选定的模型。\n'
    '注意：您还可以选择以前保存的合奏。'
)
CHOSEN_PROCESS_METHOD_HELP = (
    '选择处理方法：\n'
    '从各种人工智能网络和算法中选择以处理您的轨道：\n'
    '\n'
    '• VR 架构：使用幅度谱图进行源分离。\n'
    '• MDX-Net：采用混合谱图网络进行源分离。\n'
    '• Demucs v3：也使用混合谱图网络进行源分离。\n'
    '• 合奏模式：将多个模型和网络的结果合并以获得最佳结果。\n'
    '• 音频工具：附加方便的其他实用工具。'
)


# 将GUI部分改为中文

INPUT_FOLDER_ENTRY_HELP = (
    '选择输入文件:\n'
    '选择你想要处理的音频文件.'
)
INPUT_FOLDER_ENTRY_HELP_2 = (
    '输入选项菜单:\n'
    '点击以访问输入选项菜单.'
)
OUTPUT_FOLDER_ENTRY_HELP = (
    '选择输出文件:\n'
    '选择要保存处理后文件的目录.'
)
INPUT_FOLDER_BUTTON_HELP = (
    '打开输入文件夹按钮:\n'
    '打开包含所选输入音频文件的目录.'
)
OUTPUT_FOLDER_BUTTON_HELP = (
    '打开输出文件夹按钮:\n'
    '打开所选输出文件夹.'
)
CHOOSE_MODEL_HELP = (
    '每种处理方法都有自己的一组选项和模型。\n'
    '在此处选择与所选处理方法相关的模型。'
)
FORMAT_SETTING_HELP = 'Save Outputs As: '
SECONDARY_MODEL_ACTIVATE_HELP = (
    '启用后，应用程序将使用上面选择的模型执行附加推理。'
)
SECONDARY_MODEL_HELP = (
    '选择次要模型：\n'
    '选择你想要用当前方法处理的与主干相关的次要模型。'
)

INPUT_SEC_FIELDS_HELP = (
    '右键单击此处选择您的输入！'
)

SECONDARY_MODEL_SCALE_HELP = ('该比例决定了主要模型和次要模型之间最终音频输出的平均方式。\n\n例如：\n\n'
                             '• 10% - 主模型结果的 10% 将计入最终结果。\n'
                             '• 50% - 主模型和次模型的结果将平均。\n'
                             '• 90% - 主模型结果的 90% 将计入最终结果。')
PRE_PROC_MODEL_ACTIVATE_HELP = (
    '启用后，应用程序将使用所选模型来隔离乐器部分。\n'
    '随后，所有非人声部分将从这个生成的乐器部分中提取出来。\n'
    '\n'
    '关键点：\n'
    '• 此功能可以显著减少非人声部分中的人声渗漏。\n'
    '• 仅在Demucs工具中独家提供。\n'
    '• 仅与非人声和非乐器部分输出兼容。\n'
    '• 预计总处理时间会增加。\n'
    '• 只有VR或MDX-Net Vocal Instrumental/Vocals模型可以被选择用于此过程。'
)

      
AUDIO_TOOLS_HELP = (
    'Select from various audio tools to process your track:\n'
    '\n'
    '• Manual Ensemble: Requires 2 or more selected files as inputs. This allows tracks to be processed using the algorithms from Ensemble Mode.\n'
    '• Time Stretch: Adjust the playback speed of the selected inputs to be faster or slower.\n'
    '• Change Pitch: Modify the pitch of the selected inputs.\n'
    '• Align Inputs: Choose 2 audio file and the application will align them and provide the difference in alignment.\n'
    '    - This tool provides similar functionality to "Utagoe."\n'
    '    - Primary Audio: This is usually a mixture.\n'
    '    - Secondary Audio: This is usually an instrumental.\n'
    '• Matchering: Choose 2 audio files. The matchering algorithm will master the target audio to have the same RMS, FR, peak amplitude, and stereo width as the reference audio.'
)
             
PRE_PROC_MODEL_INST_MIX_HELP = '启用后，应用程序将生成一个没有选定的音轨和人声的第三个输出。'
MODEL_SAMPLE_MODE_HELP = ('允许用户只处理曲目的一部分，以样本设置或模型，而无需进行完整的转换。\n\n注意：\n\n'
                          '• 括号中的数字是生成的样本将是的当前秒数。\n'
                          '• 您可以在“附加设置”菜单中选择从曲目中提取的秒数。')

POST_PROCESS_THREASHOLD_HELP = ('允许用户控制Post_process选项的强度。\n\n注意：\n\n'
                                '• 较高的值可能会去除更多的伪影。然而，渗漏可能会增加。\n'
                                '• 较低的值限制了伪影的去除。')

BATCH_SIZE_HELP = ('指定一次要处理的批次数量。\n\n注意：\n\n'
                   '• 较高的值意味着更多的RAM使用，但处理时间稍快。\n'
                   '• 较低的值意味着较少的RAM使用，但处理时间稍长。\n'
                   '• 批次大小值对输出质量没有影响。')
         
VR_MODEL_NOUT_HELP = ""
VR_MODEL_NOUT_LSTM_HELP = ""
  
IS_PHASE_HELP = '选择次要音频的阶段。\n• 注意：强烈建议使用"自动"选项。'
IS_ALIGN_TRACK_HELP = '启用此选项以保存对齐后的次要轨道。'
IS_MATCH_SILENCE_HELP = (
    '将次要音频的初始静音与主音频对齐。\n'
    '• 注意：如果主音频仅以人声开始，避免使用此选项。'
)
IS_MATCH_SPEC_HELP = '根据主音频的频谱图对齐次要音频。\n• 注意：这可能在特定情况下增强对齐。'

TIME_WINDOW_ALIGN_HELP = (
                           '此设置确定对齐分析的窗口大小，特别是对于具有微小时间变化的对：\n'
                           '\n'
                           '• 无：禁用时间窗口分析。\n'
                           '• 1：通过0.0625秒的窗口分析对。\n'
                           '• 2：通过0.125秒的窗口分析对。\n'
                           '• 3：通过0.25秒的窗口分析对。\n'
                           '• 4：通过0.50秒的窗口分析对。\n'
                           '• 5：通过0.75秒的窗口分析对。\n'
                           '• 6：通过1秒的窗口分析对。\n'
                           '• 7：通过2秒的窗口分析对。\n'
                           '\n'
                           '移位选项：\n'
                           '• 低：通过0.0625和0.5秒的窗口循环，以找到最佳匹配。\n'
                           '• 中：通过0.0625、0.125和0.5秒的窗口循环，以找到最佳匹配。\n'
                           '• 高：通过0.0625、0.125、0.25和0.5秒的窗口循环，以找到最佳匹配。\n'
                           '\n'
                           '需要考虑的重要点：\n'
                           '    - 使用"移位"选项可能需要更多的处理时间，并且可能无法保证更好的结果。\n'
                           '    - 选择较小的分析窗口可能会增加处理时间。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而变化。'
)

INTRO_ANALYSIS_ALIGN_HELP = (
                           '此设置确定要分析的音频输入的初始对齐的部分。\n'
                           '\n'
                           '• 默认：分析音频总长度的10%（或1/10）。\n'
                           '• 1：分析音频总长度的12.5%（或1/8）。\n'
                           '• 2：分析音频总长度的16.67%（或1/6）。\n'
                           '• 3：分析音频总长度的25%（或1/4）。\n'
                           '• 4：分析音频总长度的50%（或一半）。\n'
                           '\n'
                           '移位选项：\n'
                           '• 低：循环通过2个介绍分析值。\n'
                           '• 中：循环通过3个介绍分析值。\n'
                           '• 高：循环通过5个介绍分析值。\n'
                           '\n'
                           '需要考虑的重要点：\n'
                           '    - 使用"移位"选项将需要更多的处理时间，并且可能无法保证更好的结果。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而变化。'
)

VOLUME_ANALYSIS_ALIGN_HELP = (
                           '此设置指定要对次要输入进行的音量调整：\n'
                           '\n'
                           '• 无：不进行音量调整。\n'
                           '• 低：分析音频在4dB范围内，以1dB的增量进行调整。\n'
                           '• 中：分析音频在6dB范围内，以1dB的增量进行调整。\n'
                           '• 高：分析音频在6dB范围内，以0.5dB的增量进行调整。\n'
                           '• 非常高：分析音频在10dB范围内，以0.5dB的增量进行调整。\n'
                           '\n'
                           '需要考虑的重要点：\n'
                           '    - 选择更广泛的分析选项（例如，高，非常高）将导致处理时间更长。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而变化。'
)

PHASE_SHIFTS_ALIGN_HELP = (
                           '此设置指定要对次要输入进行的相位调整：\n'
                           '\n'
                           '移位选项：\n'
                           '• 无：不进行相位调整。\n'
                           '• 非常低：分析音频在2个不同的相位位置的范围内。\n'
                           '• 低：分析音频在4个不同的相位位置的范围内。\n'
                           '• 中：分析音频在8个不同的相位位置的范围内。\n'
                           '• 高：分析音频在18个不同的相位位置的范围内。\n'
                           '• 非常高：分析音频在36个不同的相位位置的范围内。\n'
                           '• 最大：分析音频在所有360个相位位置。\n'
                           '\n'
                           '需要考虑的重要点：\n'
                           '    - 此选项只适用于时间校正。\n'
                           '    - 如果输入之一来自模拟源，此选项可能会有所帮助。\n'
                           '    - 选择更广泛的分析选项（例如，高，非常高）将导致处理时间更长。\n'
                           '    - 选择"最大"可能需要几个小时的处理时间。\n'
                           '    - 最佳设置可能会根据正在处理的特定曲目而变化。'
)


# Warning Messages
STORAGE_ERROR = '存储不足', '主驱动器上的存储空间不足，无法继续。为了使此应用程序正常运行，您的主驱动器必须至少有 3 GB 的存储空间。\n\n请确保您的主驱动器至少有 3 GB 的存储空间，然后重试。\n\n'
STORAGE_WARNING = '可用存储空间低', '主驱动器的存储空间不足。为了使此应用程序正常运行，您的主驱动器必须至少有 3 GB 的存储空间。\n\n'
CONFIRM_WARNING = '\n您确定要继续吗？'
PROCESS_FAILED = '进程失败，请查看错误日志\n'
EXIT_PROCESS_ERROR = '活动进程', '在退出之前，请停止活动进程或等待其完成。'
EXIT_HALTED_PROCESS_ERROR = '停止进程', '在退出之前，请等待应用程序完成停止进程。'
EXIT_DOWNLOAD_ERROR = '活动下载', '在退出之前，请停止下载或等待其完成。'
SET_TO_DEFAULT_PROCESS_ERROR = '活动进程', '在活动进程期间无法重置所有应用程序设置。'
SET_TO_ANY_PROCESS_ERROR = '活动进程', '在活动进程期间无法重置应用程序设置。'
RESET_ALL_TO_DEFAULT_WARNING = '重置设置确认', '所有应用程序设置将被重置为出厂默认设置。\n\n您确定要继续吗？'
AUDIO_VERIFICATION_CHECK = lambda i, e:f'++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n已删除损坏文件：\n\n{i}\n\n错误详细信息：\n\n{e}\n++++++++++++++++++++++++++++++++++++++++++++++++++++'
INVALID_ONNX_MODEL_ERROR = '无效模型', '所选文件不是有效的 MDX-Net 模型。请查看错误日志以获取更多信息。'
INVALID_PARAM_MODEL_ERROR = '选择模型参数', '请选择模型参数或点击\'取消\'。'
UNRECOGNIZED_MODEL = '检测到无法识别的模型', ' 是一个无法识别的模型。\n\n' + \
                     '您是否要在继续之前选择正确的参数？'
STOP_PROCESS_CONFIRM = '确认', '您即将停止所有活动进程。\n\n您确定要继续吗？'
NO_ENSEMBLE_SELECTED = '未选择任何模型', '请选择集成模型然后重试。'
PICKLE_CORRU = '文件损坏', '无法加载此集成模型。\n\n' + \
               '您是否要从列表中移除此集成模型？'
DELETE_ENS_ENTRY = '确认移除', '您确定要移除此条目吗？'


# Separation Text
LOADING_MODEL = '正在加载模型...'
INFERENCE_STEP_1 = '正在进行推理...'
INFERENCE_STEP_1_SEC = '正在进行推理（次要模型）...'
INFERENCE_STEP_1_4_STEM = lambda stem:f'正在进行推理（{stem}的次要模型）...'
INFERENCE_STEP_1_PRE = '正在进行推理（预处理模型）...'
INFERENCE_STEP_1_VOC_S = '正在分离人声...'
INFERENCE_STEP_2_PRE = lambda pm, m:f'正在加载预处理模型（{pm}：{m}）...'
INFERENCE_STEP_2_SEC = lambda pm, m:f'正在加载次要模型（{pm}：{m}）...'
INFERENCE_STEP_2_VOC_S = lambda pm, m:f'正在加载人声分离模型（{pm}：{m}）...'
INFERENCE_STEP_2_SEC_CACHED_MODOEL = lambda pm, m:f'次要模型（{pm}：{m}）的缓存已加载。\n'
INFERENCE_STEP_2_PRE_CACHED_MODOEL = lambda pm, m:f'预处理模型（{pm}：{m}）的缓存已加载。\n'
INFERENCE_STEP_2_SEC_CACHED = '正在加载缓存的次要模型源... 完成！\n'
INFERENCE_STEP_2_PRIMARY_CACHED = ' 模型缓存已加载。\n'
INFERENCE_STEP_2 = '推理完成。'
INFERENCE_STEP_DEVERBING = ' 正在去除混响...'
SAVING_STEM = '正在保存', ' 音轨...'
SAVING_ALL_STEMS = '正在保存所有音轨...'
ENSEMBLING_OUTPUTS = '正在合成输出...'
DONE = ' 完成！\n'
ENSEMBLES_SAVED = '已保存合成的输出！\n\n'


#Additional Text
CHOOSE_PROC_METHOD_MAIN_LABEL = '选择处理方法'
SELECT_SAVED_SETTINGS_MAIN_LABEL = '选择保存的设置'
CHOOSE_MDX_MODEL_MAIN_LABEL = '选择 MDX-NET 模型'
BATCHES_MDX_MAIN_LABEL = '批量大小'
VOL_COMP_MDX_MAIN_LABEL = '音量补偿'
SEGMENT_MDX_MAIN_LABEL = '分段大小'
SELECT_VR_MODEL_MAIN_LABEL = '选择VR模型'
AGGRESSION_SETTING_MAIN_LABEL = '侵略性设置'
WINDOW_SIZE_MAIN_LABEL = '窗口大小'
CHOOSE_DEMUCS_MODEL_MAIN_LABEL = '选择 Demucs 模型'
CHOOSE_STEMS_MAIN_LABEL = '选择音轨'
CHOOSE_SEGMENT_MAIN_LABEL = '分段大小'
CHOOSE_ENSEMBLE_MAIN_LABEL = '选择合奏'
CHOOSE_MAIN_PAIR_MAIN_LABEL = '主音轨对'
CHOOSE_ENSEMBLE_ALGORITHM_MAIN_LABEL = '选择合奏算法'
AVAILABLE_MODELS_MAIN_LABEL = '可用模型'
CHOOSE_AUDIO_TOOLS_MAIN_LABEL = '选择音频工具'
CHOOSE_MANUAL_ALGORITHM_MAIN_LABEL = '选择算法'
CHOOSE_RATE_MAIN_LABEL = '速率'
CHOOSE_SEMITONES_MAIN_LABEL = '半音'
GPU_CONVERSION_MAIN_LABEL = 'GPU 转换'
ENSEMBLE_OPTIONS_MAIN_LABEL = '合奏选项'
CHANGE_LOG_HEADER = lambda patch:f"补丁版本:\n\n{patch}"
INVALID_INPUT_E = ' 无效输入! '
LB_UP = "向上移动选择"
LB_DOWN = "向下移动选择"
LB_CLEAR = "清除框"
LB_MOVE_OVER_P = "将选择移动到次要列表"
LB_MOVE_OVER_S = "将选择移动到主要列表"
FILE_ONE_MAIN_LABEL = "主音频"
FILE_TWO_MAIN_LABEL = "次要音频"
FILE_ONE_MATCH_MAIN_LABEL = "目标音频"
FILE_TWO_MATCH_MAIN_LABEL = "参考音频"
TIME_WINDOW_MAIN_LABEL = "时间调整"
INTRO_ANALYSIS_MAIN_LABEL = "介绍分析"
VOLUME_ADJUSTMENT_MAIN_LABEL = "音量调节"
SELECT_INPUTS = "选择输入文件(s)"
SELECTED_INPUTS = '选定的输入'
WIDEN_BOX = '加宽界面'
CONFIRM_ENTRIES = '确认条目'
CLOSE_WINDOW = '关闭窗口'
DUAL_AUDIO_PROCESSING = '双音频批处理'
CANCEL_TEXT = "取消"
CONFIRM_TEXT = "确认"
SELECT_MODEL_TEXT = '选择模型'
NONE_SELECTED = '未选择'
SAVE_TEXT = '保存'
OVERLAP_TEXT = '重叠'
ACCEPT_ANY_INPUT_TEXT = '接受任何输入'
ACTIVATE_PRE_PROCESS_MODEL_TEXT = '激活预处理模型'
ACTIVATE_SECONDARY_MODEL_TEXT = '激活次要模型'
ADDITIONAL_MENUS_INFORMATION_TEXT = '其他菜单和信息'
ADDITIONAL_SETTINGS_TEXT = '附加设置'
ADVANCED_ALIGN_TOOL_OPTIONS_TEXT = '高级对齐工具选项'
ADVANCED_DEMUCS_OPTIONS_TEXT = '高级Demucs选项'
ADVANCED_ENSEMBLE_OPTIONS_TEXT = '高级合奏选项'
ADVANCED_MDXNET23_OPTIONS_TEXT = '高级MDX-NET23选项'
ADVANCED_MDXNET_OPTIONS_TEXT = '高级MDX-NET选项'
ADVANCED_OPTION_MENU_TEXT = '高级选项菜单'
ADVANCED_VR_OPTIONS_TEXT = '高级VR选项'
AGGRESSION_SETTING_TEXT = '侵略性设置'
APPEND_ENSEMBLE_NAME_TEXT = '附加合奏名称'
APPLICATION_DOWNLOAD_CENTER_TEXT = '应用程序下载中心'
APPLICATION_UPDATES_TEXT = '应用程序更新'
AUDIO_FORMAT_SETTINGS_TEXT = '音频格式设置'
BALANCE_VALUE_TEXT = '平衡值'
BATCH_SIZE_TEXT = '批量大小'
BV_MODEL_TEXT = 'BV模型'
CHANGE_MODEL_DEFAULT_TEXT = '更改模型默认值'
CHANGE_MODEL_DEFAULTS_TEXT = '更改模型默认值'
CHANGE_PARAMETERS_TEXT = '更改参数'
CHOOSE_ADVANCED_MENU_TEXT = '选择高级菜单'
CHOOSE_MODEL_PARAM_TEXT = '选择模型参数'
CLEAR_AUTOSET_CACHE_TEXT = '清除自动设置缓存'
COMBINE_STEMS_TEXT = '合并茎'
CONFIRM_UPDATE_TEXT = '确认更新'
COPIED_TEXT = '已复制！'
COPY_ALL_TEXT_TEXT = '复制所有文本'
DEFINED_PARAMETERS_DELETED_TEXT = '已删除定义的参数'
DELETE_PARAMETERS_TEXT = '删除参数'
DELETE_USER_SAVED_SETTING_TEXT = '删除用户保存的设置'
DEMUCS_TEXT = 'Demucs'
DENOISE_OUTPUT_TEXT = '去噪输出'
DEVERB_VOCALS_TEXT = '去除人声混响'
DONE_TEXT = '完成'
DOWNLOAD_CENTER_TEXT = '下载中心'
DOWNLOAD_CODE_TEXT = '下载代码'
DOWNLOAD_LINKS_TEXT = '下载链接'
DOWNLOAD_UPDATE_IN_APPLICATION_TEXT = '在应用程序中下载更新'
ENABLE_HELP_HINTS_TEXT = '启用帮助提示'
ENABLE_TTA_TEXT = '启用TTA'
ENABLE_VOCAL_SPLIT_MODE_TEXT = '启用人声分离模式'
ENSEMBLE_NAME_TEXT = '合奏名称'
ENSEMBLE_WAVFORMS_TEXT = '合奏波形'
ERROR_CONSOLE_TEXT = '错误控制台'
GENERAL_MENU_TEXT = '通用菜单'
GENERAL_PROCESS_SETTINGS_TEXT = '通用处理设置'
GENERATE_MODEL_FOLDER_TEXT = '生成模型文件夹'
HIGHEND_PROCESS_TEXT = '高端处理'
INPUT_CODE_TEXT = '输入代码'
INPUT_STEM_NAME_TEXT = '输入音轨名称'
INPUT_UNIQUE_STEM_NAME_TEXT = '输入唯一音轨名称'
IS_INVERSE_STEM_TEXT = '是否为反向音轨'
KARAOKE_MODEL_TEXT = '卡拉OK模型'
MANUAL_DOWNLOADS_TEXT = '手动下载'
MATCH_FREQ_CUTOFF_TEXT = '匹配频率截止'
MDXNET_C_MODEL_PARAMETERS_TEXT = 'MDX-Net C模型参数'
MDXNET_MODEL_SETTINGS_TEXT = 'MDX-Net模型设置'
MDXNET_TEXT = 'MDX-Net'
MODEL_PARAMETERS_CHANGED_TEXT = '模型参数已更改'
MODEL_SAMPLE_MODE_SETTINGS_TEXT = '模型样本模式设置'
MODEL_TEST_MODE_TEXT = '模型测试模式'
MP3_BITRATE_TEXT = 'Mp3比特率'
NAME_SETTINGS_TEXT = '名称设置'
NO_DEFINED_PARAMETERS_FOUND_TEXT = '未找到定义的参数'
NO_TEXT = '否'
NORMALIZE_OUTPUT_TEXT = '标准化输出'
USE_OPENCL_TEXT = '使用OpenCL'
NOT_ENOUGH_MODELS_TEXT = '模型不足'
NOTIFICATION_CHIMES_TEXT = '通知铃声'
OPEN_APPLICATION_DIRECTORY_TEXT = '打开应用程序目录'
OPEN_LINK_TO_MODEL_TEXT = '打开模型链接'
OPEN_MODEL_DIRECTORY_TEXT = '打开模型目录'
OPEN_MODEL_FOLDER_TEXT = '打开模型文件夹'
OPEN_MODELS_FOLDER_TEXT = '打开模型文件夹'
PHASE_SHIFTS_TEXT = '相位移位'
POST_PROCESS_TEXT = '后处理'
POST_PROCESS_THRESHOLD_TEXT = '后处理阈值'
PREPROCESS_MODEL_CHOOSE_TEXT = '预处理模型'
PRIMARY_STEM_TEXT = '主音轨'
REFRESH_LIST_TEXT = '刷新列表'
REMOVE_SAVED_ENSEMBLE_TEXT = '删除保存的合奏'
REPORT_ISSUE_TEXT = '报告问题'
RESET_ALL_SETTINGS_TO_DEFAULT_TEXT = '将所有设置重置为默认'
RESTART_APPLICATION_TEXT = '重新启动应用程序'
SAMPLE_CLIP_DURATION_TEXT = '样本剪辑时长'
SAVE_ALIGNED_TRACK_TEXT = '保存对齐的轨道'
SAVE_ALL_OUTPUTS_TEXT = '保存所有输出'
SAVE_CURRENT_ENSEMBLE_TEXT = '保存当前合奏'
SAVE_CURRENT_SETTINGS_TEXT = '保存当前设置'
SAVE_INSTRUMENTAL_MIXTURE_TEXT = '保存乐器混合'
SAVE_SPLIT_VOCAL_INSTRUMENTALS_TEXT = '保存分离的人声乐器'
SECONDARY_MODEL_TEXT = '次要模型'
SECONDARY_PHASE_TEXT = '次要阶段'
SECONDS_TEXT = '秒'
SEGMENT_DEFAULT_TEXT = '段默认'
SEGMENT_SIZE_TEXT = '段大小'
SEGMENTS_TEXT = '段'
SELECT_DOWNLOAD_TEXT = '选择下载'
SELECT_MODEL_PARAM_TEXT = '选择模型参数'
SELECT_VOCAL_TYPE_TO_DEVERB_TEXT = '选择去除混响的人声类型'
SELECTED_MODEL_PLACEMENT_PATH_TEXT = '选择的模型放置路径'
SETTINGS_GUIDE_TEXT = '设置指南'
SETTINGS_TEST_MODE_TEXT = '设置测试模式'
SHIFT_CONVERSION_PITCH_TEXT = '移位转换音高'
SHIFTS_TEXT = '移位'
SILENCE_MATCHING_TEXT = '静音匹配'
SPECIFY_MDX_NET_MODEL_PARAMETERS_TEXT = '指定MDX-Net模型参数'
SPECIFY_PARAMETERS_TEXT = '指定参数'
SPECIFY_VR_MODEL_PARAMETERS_TEXT = '指定VR模型参数'
SPECTRAL_INVERSION_TEXT = '光谱反转'
SPECTRAL_MATCHING_TEXT = '光谱匹配'
SPLIT_MODE_TEXT = '分离模式'
STEM_NAME_TEXT = '音轨名称'
STOP_DOWNLOAD_TEXT = '停止下载'
SUPPORT_UVR_TEXT = '支持UVR'
TRY_MANUAL_DOWNLOAD_TEXT = '尝试手动下载'
UPDATE_FOUND_TEXT = '找到更新'
USER_DOWNLOAD_CODES_TEXT = '用户下载代码'
UVR_BUY_ME_A_COFFEE_LINK_TEXT = 'UVR \'给我买杯咖啡\' 链接'
UVR_ERROR_LOG_TEXT = 'UVR错误日志'
UVR_PATREON_LINK_TEXT = 'UVR Patreon链接'
VOCAL_DEVERB_OPTIONS_TEXT = '人声去混响选项'
VOCAL_SPLIT_MODE_OPTIONS_TEXT = '人声分离模式选项'
VOCAL_SPLIT_OPTIONS_TEXT = '人声分离选项'
VOLUME_COMPENSATION_TEXT = '音量补偿'
VR_51_MODEL_TEXT = 'VR 5.1模型'
VR_ARCH_TEXT = 'VR架构'
WAV_TYPE_TEXT = 'Wav类型'
CUDA_NUM_TEXT = 'GPU设备'
WINDOW_SIZE_TEXT = '窗口大小'
YES_TEXT = '是'
VERIFY_INPUTS_TEXT = '验证输入'
AUDIO_INPUT_TOTAL_TEXT = '音频输入总数'
MDX23C_ONLY_OPTIONS_TEXT = '仅MDXNET23选项'
PROCESS_STARTING_TEXT = '进程开始... '
MISSING_MESS_TEXT = '缺失或损坏。'
SIMILAR_TEXT = "是相同的。"
LOADING_VERSION_INFO_TEXT = '加载版本信息...'
CHECK_FOR_UPDATES_TEXT = '检查更新'
INFO_UNAVAILABLE_TEXT = "信息不可用。"
UPDATE_CONFIRMATION_TEXT = '你确定要继续吗？\n\n应用程序需要重新启动。\n'
BROKEN_OR_INCOM_TEXT = '已移除损坏或不兼容的文件。请查看错误日志以获取详细信息。'
BMAC_UVR_TEXT = 'UVR "给我买杯咖啡" 链接'
MDX_MENU_WAR_TEXT = '（如果你不确定，就保持这个设置。）'
NO_FILES_TEXT = '没有文件'
CHOOSE_INPUT_TEXT = '选择输入'
OPEN_INPUT_DIR_TEXT = '打开输入目录'
BATCH_PROCESS_MENU_TEXT = '批处理菜单'
TEMP_FILE_DELETION_TEXT = '临时文件删除'
VOCAL_SPLITTER_OPTIONS_TEXT = '人声分离器选项'
WAVEFORM_ENSEMBLE_TEXT = '波形合奏'
SELECT_INPUT_TEXT = '选择输入文件'
SELECT_OUTPUT_TEXT = '选择输出文件'
TIME_CORRECTION_TEXT = '时间校正'
UVR_LIS_INFO_TEXT = 'UVR许可信息'
ADDITIONAL_RES_CREDITS_TEXT = '附加资源和信用'
SAVE_INST_MIXTURE_TEXT = '保存乐器混合'
DOWNLOAD_UPDATE_IN_APP_TEXT = '在应用程序中下载更新'
WAVE_TYPE_TEXT = '波形类型'
OPEN_LINK_TO_MODEL_TEXT = "打开模型链接"
OPEN_MODEL_DIRECTORY = "打开模型目录"
SELECTED_MODEL_PLACE_PATH_TEXT = '选择的模型放置路径'
IS_INVERSE_STEM_TEXT = "是否为反向音轨"
INPUT_STEM_NAME_TEXT = "输入音轨名称"
INPUT_UNIQUE_STEM_NAME_TEXT = "输入唯一音轨名称"
DONE_MENU_TEXT = "完成"
OK_TEXT = "好的"
ENSEMBLE_WARNING_NOT_ENOUGH_SHORT_TEXT = "模型不足"
ENSEMBLE_WARNING_NOT_ENOUGH_TEXT = "你必须选择2个或更多的模型来保存一个合奏。"
NOT_ENOUGH_ERROR_TEXT = "没有足够的文件进行处理。\n"
INVALID_FOLDER_ERROR_TEXT = '无效的文件夹', '你给出的导出路径不是一个有效的文件夹！'

GET_DL_VIP_CODE_TEXT = ("通过访问下面的链接之一来获取代码。"
                        "\n从那里你可以捐赠，承诺，"
                        "或者只是获取代码！\n (捐赠不是获取VIP代码的必要条件)")
CONFIRM_RESTART_TEXT = '重新启动确认', '这将重新启动应用程序并停止任何正在运行的进程。你当前的设置将被保存。 \n\n 你确定要继续吗？'
ERROR_LOADING_FILE_TEXT = '加载以下文件时出错', '原始错误详细信息'
LOADING_MODEL_TEXT = '正在加载模型'
FULL_APP_SET_TEXT = '完整的应用程序设置'
PROCESS_STARTING_TEXT = '进程开始... '
PROCESS_STOPPED_BY_USER = '\n\n用户停止了进程。'
NEW_UPDATE_FOUND_TEXT = lambda version:f"\n\n找到新更新：{version}\n\n点击\"设置\"菜单中的更新按钮来下载和安装！"
ROLL_BACK_TEXT = '点击这里回滚'


def secondary_stem(stem:str):
    """Determines secondary stem"""
    
    stem = stem if stem else NO_STEM
    
    if stem in STEM_PAIR_MAPPER.keys():
        for key, value in STEM_PAIR_MAPPER.items():
            if stem in key:
                secondary_stem = value
    else:
        secondary_stem = stem.replace(NO_STEM, "") if NO_STEM in stem else f"{NO_STEM}{stem}"
    
    return secondary_stem
