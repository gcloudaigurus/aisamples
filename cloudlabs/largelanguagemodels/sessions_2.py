
import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the Transformer model
class Transformer(nn.Module):
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout=0.1):
        super(Transformer, self).__init__()
        # Encoder layers
        self.encoder = nn.TransformerEncoder(nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout), num_encoder_layers)
        # Decoder layers
        self.decoder = nn.TransformerDecoder(nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout), num_decoder_layers)
        # Embedding layers
        self.src_emb = nn.Embedding(src_vocab_size, d_model)
        self.tgt_emb = nn.Embedding(tgt_vocab_size, d_model)
        # Linear layer for output
        self.fc_out = nn.Linear(d_model, tgt_vocab_size)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None, memory_mask=None, src_key_padding_mask=None, tgt_key_padding_mask=None, memory_key_padding_mask=None):
        # Pass source through encoder
        src_emb = self.src_emb(src) * (self.src_emb.embedding_dim ** 0.5) #Scaling embedding
        encoder_out = self.encoder(src_emb, mask=src_mask, src_key_padding_mask=src_key_padding_mask)
        # Pass target through decoder
        tgt_emb = self.tgt_emb(tgt) * (self.tgt_emb.embedding_dim ** 0.5) #Scaling embedding
        decoder_out = self.decoder(tgt_emb, encoder_out, tgt_mask=tgt_mask, memory_mask=memory_mask, tgt_key_padding_mask=tgt_key_padding_mask, memory_key_padding_mask=memory_key_padding_mask)
        # Output layer
        output = self.fc_out(decoder_out)
        return output

# Generate sample data (replace with your actual data)
src_vocab_size = 100
tgt_vocab_size = 100
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
batch_size = 32
src_len = 20
tgt_len = 20

src = torch.randint(0, src_vocab_size, (batch_size, src_len))
tgt = torch.randint(0, tgt_vocab_size, (batch_size, tgt_len))

# Initialize the model
model = Transformer(src_vocab_size, tgt_vocab_size, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward)

# Generate masks (optional, but important for longer sequences)
src_mask = None  #Generate appropriate mask if needed
tgt_mask = None # Generate appropriate mask if needed

# Forward pass
output = model(src, tgt, src_mask=src_mask, tgt_mask=tgt_mask)

# Print output shape (this is just a simple check, actual training and evaluation require loss functions and optimizers)
print(output.shape) #Should be (batch_size, tgt_len, tgt_vocab_size)

#Example of creating a simple mask (Padding Mask)
src_padding_mask = (src == 0).transpose(0,1)


