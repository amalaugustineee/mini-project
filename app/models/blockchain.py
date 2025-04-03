from app import db
import json

class BlockchainData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    block_index = db.Column(db.Integer, nullable=False)
    block_data = db.Column(db.Text, nullable=False)  # Store block data as JSON
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'block_index': self.block_index,
            'block_data': json.loads(self.block_data),
            'created_at': self.created_at.isoformat()
        }

    @staticmethod
    def from_dict(data):
        return BlockchainData(
            block_index=data['index'],
            block_data=json.dumps(data)
        ) 