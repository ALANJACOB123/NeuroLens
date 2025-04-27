# Stream EEG data from BrainFlow

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import time

def acquire_eeg(duration_sec=60):
    params = BrainFlowInputParams()
    params.serial_port = '/dev/ttyUSB0'  # Adjust as needed
    board = BoardShim(BoardIds.MUSE_2.value, params)

    board.prepare_session()
    board.start_stream()
    time.sleep(duration_sec)
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()
    return data
