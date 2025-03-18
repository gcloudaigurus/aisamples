import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import {
  Box,
  Typography,
  Card,
  CardContent,
  Grid,
  List,
  ListItem,
  ListItemText,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  CircularProgress,
  Alert,
  Divider,
} from '@mui/material';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

const CourseDetails = () => {
  const { id } = useParams();
  const { user } = useAuth();
  const [course, setCourse] = useState(null);
  const [assignments, setAssignments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    dueDate: '',
  });

  useEffect(() => {
    fetchData();
  }, [id]);

  const fetchData = async () => {
    try {
      const [courseRes, assignmentsRes] = await Promise.all([
        axios.get(`/api/courses/${id}`),
        axios.get(`/api/courses/${id}/assignments`)
      ]);

      setCourse(courseRes.data);
      setAssignments(assignmentsRes.data);
    } catch (err) {
      setError('Failed to load course details');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleOpenDialog = () => {
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
    setFormData({
      title: '',
      description: '',
      dueDate: '',
    });
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleCreateAssignment = async () => {
    try {
      await axios.post('/api/assignments', {
        ...formData,
        courseId: id
      });
      fetchData();
      handleCloseDialog();
    } catch (err) {
      setError('Failed to create assignment');
      console.error(err);
    }
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="200px">
        <CircularProgress />
      </Box>
    );
  }

  if (!course) {
    return (
      <Alert severity="error">
        Course not found
      </Alert>
    );
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        {course.title}
      </Typography>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Course Information
              </Typography>
              <Typography variant="body1" paragraph>
                <strong>Instructor:</strong> {course.instructor}
              </Typography>
              <Typography variant="body1" paragraph>
                <strong>Description:</strong> {course.description}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
                <Typography variant="h6">
                  Assignments
                </Typography>
                {user.role === 'admin' && (
                  <Button
                    variant="contained"
                    color="primary"
                    onClick={handleOpenDialog}
                  >
                    Add Assignment
                  </Button>
                )}
              </Box>
              {assignments.length === 0 ? (
                <Typography color="textSecondary">
                  No assignments yet.
                </Typography>
              ) : (
                <List>
                  {assignments.map((assignment) => (
                    <div key={assignment.id}>
                      <ListItem>
                        <ListItemText
                          primary={assignment.title}
                          secondary={`Due: ${new Date(assignment.dueDate).toLocaleDateString()}`}
                        />
                      </ListItem>
                      <Divider />
                    </div>
                  ))}
                </List>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Add Assignment Dialog */}
      <Dialog open={openDialog} onClose={handleCloseDialog}>
        <DialogTitle>Add New Assignment</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            name="title"
            label="Assignment Title"
            type="text"
            fullWidth
            value={formData.title}
            onChange={handleInputChange}
          />
          <TextField
            margin="dense"
            name="description"
            label="Description"
            type="text"
            fullWidth
            multiline
            rows={4}
            value={formData.description}
            onChange={handleInputChange}
          />
          <TextField
            margin="dense"
            name="dueDate"
            label="Due Date"
            type="date"
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
            value={formData.dueDate}
            onChange={handleInputChange}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancel</Button>
          <Button onClick={handleCreateAssignment} color="primary">
            Create
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default CourseDetails; 