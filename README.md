# CollabChain: Onchain Collaborative Planning Platform

## Overview

CollabChain is an onchain collaborative planning platform for supply chain partners to coordinate promotions, product launches, and data sharing agreements using smart contracts.

## Project Structure

- `contracts/`: Contains Solidity smart contracts for blockchain functionality.
- `backend/`: Python Flask backend to interact with the blockchain.
- `frontend/`: HTML, CSS, and JavaScript for the user interface.
- `test/`: Testing files for smart contracts and backend.

## Prerequisites

- Python 3.x
- Node.js and npm
- MetaMask wallet

## Setup Instructions

### Backend Setup

1. Navigate to the `backend` directory:

   ```sh
   cd backend
   ```

2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask server:

   ```sh
   python app.py
   ```

### Frontend Setup

1. Navigate to the root directory and open `index.html` in your browser.

### Smart Contract Deployment

1. Use Remix IDE or Hardhat to deploy `EventContract.sol` and `DataAgreementContract.sol` to the Base Sepolia testnet.

### Configuration

- **Contract Addresses**: Update `event_contract_address` and `agreement_contract_address` in `backend/app.py` with the deployed contract addresses.
- **Provider URL**: Update the Base Sepolia testnet URL in `backend/config.py`.
- **Wallet Setup**: Use MetaMask to connect to the Base Sepolia testnet and obtain some test ETH from a faucet for transaction fees.

### Testing

- Run the tests for smart contracts:

  ```sh
  brownie test
  ```

- Run the Flask tests:

  ```sh
  pytest ../test/test_flask_app.py
  ```

## Usage

- Create and manage events onchain.
- Propose and accept data sharing agreements securely.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request.

## License

MIT License
